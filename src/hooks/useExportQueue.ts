import { useState } from "react";
import { arrayToCSV, exportTablesAsZip } from "../utils/csv_zip";

export interface TableEntry {
  name: string;
  data: string[][];
}

export function useExportQueue() {
  const [tables, setTables] = useState<TableEntry[]>([]);

  const addTable = (entry: TableEntry) => {
    setTables(prev => [...prev, entry]);
  };

  const reset = () => {
    setTables([]);
  }

  const uploadToBackend = async () => {
    for (const { name, data } of tables) {
      const csv = arrayToCSV(data);
      const blob = new Blob([csv], { type: "text.csv" });
      const formData = new FormData();
      formData.append("file", blob, `${name}.csv`);

      try {
        const res = await fetch("https://localhost:51000/upload_csv/", {
          method: "POST",
          body: formData,
        });

        if (!res.ok) {
          console.error(`Failed to upload ${name}`);
        } else {
          const result = await res.json();
          console.log(`Uploaded ${name}:`, result);
        }

        reset();
      } catch (err) {
        console.error("Upload failed:", err);
      }
    }
  }

  return { tables, addTable, reset, uploadToBackend };
}