import JSZip from "jszip";
import { saveAs } from "file-saver";
import type { TableEntry } from "../hooks/useExportQueue";

export function arrayToCSV(data: string[][]): string {
  return data.map(row =>
    row.map(cell => `"${String(cell ?? "").replace(/"/g, '""')}"`).join(",")
  ).join("\n");
}

export async function exportTablesAsZip(tables: TableEntry[]) {
  const zip = new JSZip();
  for (const { name, data } of tables) {
    console.log("array to CSV", name);
    zip.file(`${name}.csv`, arrayToCSV(data));
  }
  const blob = await zip.generateAsync({ type: "blob" });
  saveAs(blob, "exported_tables.zip");
}