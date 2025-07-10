export type ExcelData = {
  sheet: string;
  address: string;
  data: any[][];
}

export async function getExcelData(): Promise<ExcelData | null> {
  try {
    return await Excel.run(async (context) => {
      const range = context.workbook.getSelectedRange();

      range.load("address, values, worksheet/name");
      await context.sync();

      let result: ExcelData = {
        sheet: range.worksheet.name,
        address: range.address,
        data: range.values,
      };

      return result;
    });
  } catch (error) {
    console.error("[getExcelData] Error: "+ error);
    return null;
  }
}

export function ffillRowWise(data: any[][]): any[][] {
  return data.map((row) => {
    const filledRow: any[] = [];
    let lastValid = null;

    for (let i = 0; i < row.length; i++) {
      const value = row[i];
      if (value !== null && value !== "") {
        lastValid = value;
        filledRow.push(value);
      } else {
        filledRow.push(lastValid);
      }
    }

    return filledRow;
  });
}

export function ffillColWise(data: any[][]): any[][] {
  const filled = [...data.map(row => [...row])]; // deep clone

  const numRows = filled.length;
  const numCols = filled[0]?.length ?? 0;

  for (let col = 0; col < numCols; col++) {
    let lastValid = null;
    for (let row = 0; row < numRows; row++) {
      const val = filled[row][col];
      if (val !== null && val !== "") {
        lastValid = val;
      } else {
        filled[row][col] = lastValid;
      }
    }
  }

  return filled;
}