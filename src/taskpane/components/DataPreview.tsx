import * as React from "react";
import { Button } from "@fluentui/react-components";
import { makeStyles } from "@fluentui/react-components";
import { ExcelData } from "../../utils/data_ops";
import { useExcelData } from "../../hooks/useExcelData";
import { useExportQueue } from "../../hooks/useExportQueue";
import ExcelPreview from "./ExcelPreview";

interface DataPreviewProps {
  dataHandler: () => Promise<ExcelData | null>;
}

const useStyles = makeStyles({
  // Category button
  categorySelector: {
    display: "flex",
    justifyContent: "center",
    gap: "8px",
    marginBottom: "12px",
  },
  selected: {
    backgroundColor: "#d0d0d0", // 선택된 버튼 강조
  },
  // Data preview button
  dataQueryPreview: {
    display: "flex",
    flexDirection: "column",
    justifyContent: "space-between",
    minHeight: "20vh",
    alignItems: "center",
    gap: "16px",
    marginBottom: "20px"
  },
  infoRow: {
    display: "flex",
    flexDirection: "row",
    alignItems: "flex-start",
    justifyContent: "flex-start",
    gap: "24px", // Space between button and text
  },
  table: {
    maxHeight: "300px",
    overflowY: "auto",
    overflowX: "auto",
    width: "100%",
  },
  actionRow: {
    display: "flex",
    flexDirection: "row",
    justifyContent: "center", // 버튼들을 가운데 정렬
    alignItems: "center",
    gap: "12px",
    marginTop: "auto",         // 여유 공간 밀어내기
    paddingTop: "20px",
  },
  infoText: {
    display: "flex",
    flexDirection: "column",
    fontWeight: 500,
  },
});

const categories = ["오피스", "리테일", "물류창고", "호텔"];

const DataPreview: React.FC<DataPreviewProps> = (_: DataPreviewProps) => {
  const [prefix, setPrefix] = React.useState("오피스");

  const { data, sheetName, rangeInfo, loading, handleGetRange } = useExcelData();
  const { tables, addTable, reset, uploadToBackend } = useExportQueue();
  const styles = useStyles();

  return (
    <div className={styles.dataQueryPreview}>
      {/* Category Selector */}
      <div className={styles.categorySelector}>
        {categories.map((cat) => (
          <Button
            key={cat}
            size="medium"
            appearance={cat === prefix ? "primary" : "secondary"}
            className={cat === prefix ? styles.selected : ""}
            onClick={() => setPrefix(cat)}
          >
            {cat}
          </Button>
        ))}
      </div>
      {/* Get Range */}
      <div className={styles.infoRow}>
        <div className={styles.actionRow}>
          <Button size="large" onClick={handleGetRange} disabled={loading}>
            {loading ? "Reading..." : "Get Selected Excel Range"}
          </Button>
          <div className={styles.infoText}>
            <div><strong>Sheet:</strong> {sheetName ?? "-"}</div>
            <div><strong>Range:</strong> {rangeInfo ?? "-"}</div>
          </div>
        </div>
      </div>

      {data.length > 0 ? (
        <div className={styles.table}>
          <ExcelPreview data={data} />
        </div>
      ) : (
        <div className={styles.table}>
          <p>No data loaded. Select a range and click "Get Selected Excel Range".</p>
        </div>
      )}

      <div className={styles.actionRow}>
        <Button
          appearance="secondary"
          size="large"
          disabled={data.length === 0}
          onClick={() => {
            const name = `${sheetName}_${rangeInfo}`.replace(/[^a-zA-Z0-9-_]/g, "_");
            addTable({ prefix, name, data });
          }}
        >
          Add to Queue
        </Button>

        <Button
          appearance="secondary"
          size="large"
          disabled={tables.length === 0}
          onClick={reset}
        >
          Reset Queue
        </Button>

        <Button
          appearance="outline"
          size="large"
          disabled={tables.length === 0}
          onClick={uploadToBackend}
        >
          Save
        </Button>
      </div>
    </div>
  )
}

export default DataPreview;