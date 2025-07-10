import { useState } from "react"
import { getExcelData } from "../utils/data_ops";
import { etoi, itoe, move } from "../utils/cell_ops";
import { analyzeSelectedArea, findDataStart, findFirstColoredCellLRTD, findFirstRowWithBorder } from "../utils/find_header";
import { moveToSelectedRange } from "../utils/render";

export const useExcelData = () => {
  const [sheetName, setSheetName] = useState("");
  const [rangeInfo, setRangeInfo] = useState("");
  const [data, setData] = useState<any[][]>([]);
  const [loading, setLoading] = useState(false);

  const handleGetRange = async () => {
    setLoading(true);
    try {
      const values = await getExcelData();
      let area = etoi(values.address);
      const discov = await analyzeSelectedArea();
      
      const nonTableOffset = findFirstColoredCellLRTD(discov.cellColor);
      const headerOffset = findDataStart(discov.mergedInfo);
      const footerOffset = findFirstRowWithBorder(discov.cellBorder, "bottom");
      
      console.log("nonTableOffset", nonTableOffset);
      console.log("headerOffset", headerOffset);
      console.log("footerOffset", footerOffset);

      let dataWithHeader = move(area, { start: nonTableOffset });
      let dataWithoutHeader = move(dataWithHeader, { start: headerOffset });
      let dataWithoutFooter = move(dataWithoutHeader, { end: footerOffset });

      await moveToSelectedRange(itoe(dataWithoutFooter));
      const revised = await getExcelData();

      setSheetName(revised.sheet);
      setRangeInfo(revised.address);
      setData(revised.data);
    } catch (err) {
      console.error("Failed to read data", err);
    }
    setLoading(false);
  };

  return { data, sheetName, rangeInfo, loading, handleGetRange };
}