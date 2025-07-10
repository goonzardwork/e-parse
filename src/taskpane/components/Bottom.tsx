import * as React from "react";
import { Image, tokens, makeStyles } from "@fluentui/react-components";

export interface BottomProps {
  // Use it in the future
}

const useStyles = makeStyles({
  welcome__header: {
    display: "flex",
    flexDirection: "row", // side by side
    alignItems: "center",
    justifyContent: "center",
    gap: "16px",
    padding: "24px 16px",
    backgroundColor: tokens.colorNeutralBackground3,
  },
});

const Bottom: React.FC = (_: BottomProps) => {
    const style = useStyles();

    return (
        <section className={style.welcome__header} />
    )
}

export default Bottom;