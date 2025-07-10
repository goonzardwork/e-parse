import { makeStyles, Table, TableBody, TableCell, TableHeader, TableHeaderCell, TableRow } from "@fluentui/react-components";
import * as React from "react";
import { renderTruncatedRow } from "../../utils/render";

interface ExcelTableProps {
  data: any[][];
}

const useStyles = makeStyles({
  cell: {
    minWidth: "20px",
    overflow: "hidden",
    textOverflow: "ellipsis",
    whiteSpace: "nowrap",
  },
});

const ExcelPreview: React.FC<ExcelTableProps> = ({ data }) => {
  const style = useStyles();
  return (
    <Table>
      <TableHeader>
        <TableRow>
          {renderTruncatedRow(data[0], (val, _, key) => (
            <TableHeaderCell className={style.cell} key={key}>{val}</TableHeaderCell>
          ))}
        </TableRow>
      </TableHeader>
      <TableBody>
        {data.slice(1).map((row, i) => (
          <TableRow key={i}>
            {renderTruncatedRow(row, (val, _, key) => (
              <TableCell className={style.cell} key={key}>{String(val)}</TableCell>
            ))}
          </TableRow>
        ))}
      </TableBody>
    </Table>
  );
};

export default ExcelPreview;