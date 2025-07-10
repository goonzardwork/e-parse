export function renderTruncatedRow(
  row: any[],
  cellRenderer: (value: any, index: number, key: string | number) => React.ReactNode
): React.ReactNode[] {
  const result: React.ReactNode[] = [];
  const colCount = row.length;

  if (colCount <= 6) {
    return row.map((val, i) => cellRenderer(val, i, i));
  }

  const lastIdx = colCount - 1;

  for (let i = 0; i < colCount; i++) {
    if (i < 4) {
      result.push(cellRenderer(row[i], i, i));
    } else if (i === 4) {
      result.push(cellRenderer("...", i, "ellipsis"));
    } else if (i === lastIdx) {
      result.push(cellRenderer(row[i], i, i));
    }
    // Skip the rest
  }

  return result;
}

export async function moveToSelectedRange(focus: string) {
  try {
    await Excel.run(async (context) => {
      const sheet = context.workbook.worksheets.getActiveWorksheet();
      const range = sheet.getRange(focus);
      range.select();

      await context.sync();
    })
  } catch (error) {
    console.error("[moveToSelectedRange] Error: ", error);
  }
}