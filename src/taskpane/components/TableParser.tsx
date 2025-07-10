import * as React from "react";
import { useState } from "react";
import { Button, Field, Textarea, tokens, makeStyles } from "@fluentui/react-components";
import DataPreview from "./DataPreview";
import { getExcelData } from "../../utils/data_ops";

/* global HTMLTextAreaElement */

interface TableParserProps {
  insertText: (text: string) => void;
}

const useStyles = makeStyles({
  instructions: {
    fontWeight: tokens.fontWeightSemibold,
    marginTop: "20px",
    marginBottom: "10px",
  },
  textPromptAndInsertion: {
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
    marginBottom: "20px",
  },
  textAreaField: {
    marginLeft: "20px",
    marginTop: "30px",
    marginBottom: "20px",
    marginRight: "20px",
    maxWidth: "50%",
  },
});

const TableParser: React.FC<TableParserProps> = (_: TableParserProps) => {
  const [text, setText] = useState<string>("_trade");

  const handleTextChange = async (event: React.ChangeEvent<HTMLTextAreaElement>) => {
    setText(event.target.value);
  };

  const styles = useStyles();

  return (
    <div className={styles.textPromptAndInsertion}>
      <Field className={styles.textAreaField} size="large" label="Enter output file name.">
        <Textarea appearance="filled-darker" size="medium" value={text} onChange={handleTextChange} />
      </Field>

      <DataPreview dataHandler={getExcelData} />
    </div>
  );
};

export default TableParser;
