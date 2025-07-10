export interface ExcelRangeIndex {
  sheet: string;
  start: [number, number]; // [rowIndex, colIndex]
  end: [number, number];   // [rowIndex, colIndex]
}

export function etoi(rangeStr: string): ExcelRangeIndex {
  const match = rangeStr.match(/^'?([^']+)'?!([A-Z]+[0-9]+)(?::([A-Z]+[0-9]+))?$/i);
  if (!match) throw new Error("Invalid range format");

  const [, sheetName, startCell, endCell] = match;
  const start = cellToIndex(startCell);
  const end = endCell ? cellToIndex(endCell) : start;

  return {
    sheet: sheetName,
    start,
    end,
  };
}

function cellToIndex(cell: string): [number, number] {
  const match = cell.match(/^([A-Z]+)([0-9]+)$/i);
  if (!match) throw new Error("Invalid cell format");

  const [, colLetters, rowStr] = match;
  const row = parseInt(rowStr, 10) - 1;
  const col = columnLetterToIndex(colLetters.toUpperCase());
  return [row, col];
}

function columnLetterToIndex(letters: string): number {
  let col = 0;
  for (let i = 0; i < letters.length; i++) {
    col = col * 26 + (letters.charCodeAt(i) - 64);
  }
  return col - 1;
}


export function itoe(cell: ExcelRangeIndex) {
  const startCell = indexToCell(cell.start);
  let endCell = cell.end ? indexToCell(cell.end) : startCell;

  if (startCell == endCell) {
    // Single Cell
    endCell = null;
  }

  return `'${cell.sheet}'!${startCell}${cell.end ? `:${endCell}` : ""}`;
}

// export function itoe(sheet: string, start: [number, number], end?: [number, number]): string {
//   const startCell = indexToCell(start);
//   const endCell = end ? indexToCell(end) : startCell;

//   return `'${sheet}'!${startCell}${end ? `:${endCell}` : ""}`;
// }

function indexToCell([row, col]: [number, number]): string {
  return `${columnIndexToLetter(col)}${row + 1}`;
}

function columnIndexToLetter(colIndex: number): string {
  let letters = "";
  while (colIndex >= 0) {
    letters = String.fromCharCode((colIndex % 26) + 65) + letters;
    colIndex = Math.floor(colIndex / 26) - 1;
  }
  return letters;
}

export function move(
  range: ExcelRangeIndex,
  offset: {
    start?: [number, number];
    end?: [number, number];
  }
): ExcelRangeIndex {
  const movedStart: [number, number] = offset.start
    ? [Math.max(range.start[0] + offset.start[0], 0), Math.max(range.start[1] + offset.start[1], 0)]
    : range.start;

  const movedEnd: [number, number] = offset.end
    ? [Math.max(range.end[0] + offset.end[0], 0), Math.max(range.end[1] + offset.end[1], 0)]
    : range.end;

  return {
    sheet: range.sheet,
    start: movedStart,
    end: movedEnd,
  };
}