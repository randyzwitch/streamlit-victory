import React, { ReactNode } from "react"
import {
  withStreamlitConnection,
  StreamlitComponentBase,
  Streamlit,
} from "./streamlit"
import {
  VictoryBar,
  VictoryScatter,
  VictoryChart,
} from 'victory';

/**
 * This is a React-based component template. The `render()` function is called
 * automatically when your component should be re-rendered.
 */
class MyComponent extends StreamlitComponentBase {

  public render = (): ReactNode => {
    // Arguments that are passed to the plugin in Python are accessible
    // via `this.props.args`. Here, we access the "name" arg.
    const chart_type = this.props.args["chart_type"]
    const data = this.props.args["data"]

    const renderPlot = () => {
      if (chart_type === 'bar') {
        return <VictoryBar data={data} x="quarter" y="earnings" />
      } else {
        return <VictoryScatter data={data} x="quarter" y="earnings" />
      }
    }

    return (
      <VictoryChart>
        {renderPlot()}
      </VictoryChart>
    )
  }

}

// "withStreamlitConnection" is a wrapper function. It bootstraps the
// connection between your component and the Streamlit app, and handles
// passing arguments from Python -> Component.
//
// You don't need to edit withStreamlitConnection (but you're welcome to!).
export default withStreamlitConnection(MyComponent)
