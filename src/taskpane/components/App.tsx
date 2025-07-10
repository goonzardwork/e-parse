import * as React from "react";
import Header from "./Header";
import TableParser from "./TableParser";
import Bottom from "./Bottom";

import { HeroListItem } from "./HeroList";
import { makeStyles } from "@fluentui/react-components";
import { Ribbon24Regular, LockOpen24Regular, DesignIdeas24Regular } from "@fluentui/react-icons";
import { insertText } from "../taskpane";

interface AppProps {
  title: string;
}

const useStyles = makeStyles({
  root: {
    minHeight: "1vh",
    minWidth: "500px",
  },
  logo: {
    width: "80px", // reduced logo size
    height: "auto",
  },
});


const App: React.FC<AppProps> = (props: AppProps) => {
  const styles = useStyles();
  // The list items are static and won't change at runtime,
  // so this should be an ordinary const, not a part of state.
  const listItems: HeroListItem[] = [
    {
      icon: <Ribbon24Regular />,
      primaryText: "Achieve more with Office integration",
    },
    {
      icon: <LockOpen24Regular />,
      primaryText: "Unlock features and functionality",
    },
    {
      icon: <DesignIdeas24Regular />,
      primaryText: "Create and visualize like a pro",
    },
  ];

  return (
    <div className={styles.root}>
      <Header
        logo="assets/logo-filled.png"
        title={props.title}
        message="LABORARE AD MORTEM"
      />
      <TableParser insertText={insertText} />
      <Bottom />
    </div>
  );
};

export default App;
