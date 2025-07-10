import { etoi, ExcelRangeIndex } from "./cell_ops";

export type Point = [number, number] | null;

export type MergedCell = {
  mainAddress: string;
  rowCount: number;
  colCount: number;
}

type Border = {
  top: boolean;
  bottom: boolean;
  left: boolean;
  right: boolean;
}

export type HeaderInference = {
  cellColor: string[][];
  cellBorder: Border[][];
  mergedcell: Set<string>;
  mergedInfo: Map<string, MergedCell>;
}

export async function analyzeSelectedArea(): Promise<HeaderInference | null> {
  try {
    return await Excel.run(async (context) => {
      const range = context.workbook.getSelectedRange();
      const props = range.getCellProperties({
        format: { fill: { color: true }, borders: { style: true } }
      });
      const merg = range.getMergedAreasOrNullObject().areas.load();
      range.getMergedAreasOrNullObject().areas
      let mrgSet: Set<string> = new Set();
      let mrgMap: Map<string, MergedCell> = new Map();

      await context.sync();

      let colors: string[][] = [];
      let borders: Border[][] = [];
      for (const row of props.value) {
        let rc: string[] = [];
        let rb: Border[] = [];
        for (const col of row) {
          rc.push(col.format.fill.color);
          rb.push({
            top: col.format.borders?.top?.style == "Continuous",
            bottom: col.format.borders?.bottom?.style == "Continuous",
            left: col.format.borders?.left?.style == "Continuous",
            right: col.format.borders?.right?.style == "Continuous",
          });
        }
        colors.push(rc);
        borders.push(rb);
      }

      if (!merg.isNullObject) {
        for (const m of merg.items) {
          mrgSet.add(m.address);
          mrgMap.set(m.address, {
            mainAddress: m.address,
            rowCount: m.rowCount,
            colCount: m.columnCount,
          });
        }
      }
      
      return { 
        cellColor: colors, 
        cellBorder: borders,
        mergedcell: mrgSet, 
        mergedInfo: mrgMap 
      };
    });
  } catch (error) {
    console.error("[detectHeader] Error: ", error);
    return null;
  }
}

function isColorSimilar(hex1: string, hex2: string, threshold: number = 15): boolean {
  const toRGB = (hex: string) => {
    const cleaned = hex.replace("#", "");
    return [
      parseInt(cleaned.slice(0, 2), 16),
      parseInt(cleaned.slice(2, 4), 16),
      parseInt(cleaned.slice(4, 6), 16),
    ];
  };

  const [r1, g1, b1] = toRGB(hex1);
  const [r2, g2, b2] = toRGB(hex2);

  return (
    Math.abs(r1 - r2) <= threshold &&
    Math.abs(g1 - g2) <= threshold &&
    Math.abs(b1 - b2) <= threshold
  );
}

export function findFirstColoredCellLRTD(
  colors: string[][], 
  baseColor: string = "#FFFFFF",
  targetColor: string | null = "#AEAAAA",
  withinHoriz: number = 5,
  withinVert: number = 5,
): Point | null { 
  const numRows = colors.length;
  const numCols = colors[0]?.length ?? 0;

  withinVert = Math.min(withinVert, numRows);
  withinHoriz = Math.min(withinVert, numCols);

  for (let col = 0; col < withinVert; col++) {
    for (let row = 0; row < withinHoriz; row++) {
      const color = colors[row][col]?.toUpperCase();

      if (color && color !== baseColor.toUpperCase()) {
        if (color && color == targetColor.toUpperCase()) {
          return [row, col];
        } else if (color && isColorSimilar(targetColor, color)) {
          console.log("Similar color");
          return [row, col];
        } else {
          continue;
        }
      }
    }
  }

  return null;
}

export function findFirstColoredCellTDLR(
  colors: string[][], 
  baseColor: string = "#FFFFFF",
  targetColor: string | null = "#AEAAAA",
  withinHoriz: number = 5,
  withinVert: number = 5,
): Point | null {
  const numRows = colors.length;
  const numCols = colors[0]?.length ?? 0;

  withinVert = Math.min(withinVert, numRows);
  withinHoriz = Math.min(withinVert, numCols);

  for (let row = 0; row < withinVert; row++) {
    for (let col = 0; col < withinHoriz; col++) {
      const color = colors[row][col].toUpperCase();

      if (color && color == targetColor.toUpperCase()) {
        return [row, col]
      }

      if (color !== baseColor.toUpperCase()) {
        if (color && color == targetColor.toUpperCase()) {
          return [row, col];
        } else if (color && isColorSimilar(targetColor, color)) {
          console.log("Similar color");
          return [row, col];
        } else {
          continue;
        }
      }
    }
  }

  return null;
}

export function findDataStart(range: ExcelRangeIndex, merged: Map<string, MergedCell>): [number, number] {
  let headerRow = 1;

  const startIdx = range.start;

  for (const i of Array.from(merged.values())) {
    const mergedMainCell = etoi(i.mainAddress);
    if (startIdx[0] === mergedMainCell.start[0] && headerRow < i.rowCount) {
      // Merged cell only for data block starting row (suspected header row)
      headerRow = i.rowCount;
    }
  }

  return [headerRow, 0];
}

export function findFirstRowWithBorder(
  cellBorder: { top: boolean; bottom: boolean; left: boolean; right: boolean }[][],
  side: "top" | "bottom" | "left" | "right",
  direction: "top-down" | "bottom-up" = "bottom-up",
  threshold: number = 1.0 // 1.0 means 100% of the cells in the row must match
): [number, number] {
  const numRows = cellBorder.length;
  if (numRows === 0) return [0, 0];

  const start = direction === "top-down" ? 0 : numRows - 1;
  const end = direction === "top-down" ? numRows : -1;
  const step = direction === "top-down" ? 1 : -1;

  for (let i = start; i !== end; i += step) {
    const rowBorders = cellBorder[i];
    const matched = rowBorders.filter(cell => cell[side] === true).length;
    const ratio = matched / rowBorders.length;

    if (ratio >= threshold) {
      const relative = direction === "bottom-up" ? i - numRows : i;
      return [relative + 1, 0];
    }
  }

  return [0, 0];
}

export function findFirstColWithBorder(
  cellBorder: { top: boolean; bottom: boolean; left: boolean; right: boolean }[][],
  side: "top" | "bottom" | "left" | "right",
  direction: "left-right" | "right-left" = "left-right",
  threshold: number = 1.0 // ratio of cells in column that must match
): [number, number] {
  const numRows = cellBorder.length;
  const numCols = cellBorder[0]?.length ?? 0;
  if (numCols === 0) return [0, 0];

  const colIndices = direction === "left-right"
    ? Array.from({ length: numCols }, (_, i) => i)
    : Array.from({ length: numCols }, (_, i) => numCols - 1 - i);

  for (let i = 0; i < colIndices.length; i++) {
    const col = colIndices[i];
    let matchCount = 0;

    for (let row = 0; row < numRows; row++) {
      const cell = cellBorder[row][col];
      if (cell && cell[side] === true) matchCount++;
    }

    const ratio = matchCount / numRows;
    if (ratio >= threshold) {
      const relative = direction === "right-left" ? col - numCols : col;
      return [0, relative + 1];
    }
  }

  return [0, 0];
}