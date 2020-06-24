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
  VictoryPie
} from 'victory'
import _ from 'lodash'

/**
 * This is a React-based component template. The `render()` function is called
 * automatically when your component should be re-rendered.
 */
class MyComponent extends StreamlitComponentBase {

  public render = (): ReactNode => {

    // Arguments that are passed to the plugin in Python are accessible
    // via `this.props.args`. Here, we access the "name" arg.
    const chart_type = this.props.args["chart_type"]

    //suggestion from Lauren via email
    const chartPropList = [
      "animate",
      "backgroundComponent",
      "children",
      "containerComponent",
      "domain",
      "domainPadding",
      "endAngle",
      "events",
      "externalEventMutations",
      "groupComponent",
      "height",
      "horizontal",
      "innerRadius",
      "maxDomain",
      "minDomain",
      "padding",
      "polar",
      "range",
      "scale",
      "sharedEvents",
      "singleQuadrantDomainPadding",
      "standalone",
      "startAngle",
      "style",
      "theme",
      "width"
    ]
    const commonProps = [
      "categories",
      "containerComponent",
      "data",
      //"dataComponent", // having this set as None from Python makes React error
      "eventKey",  //not commonly used
      //"groupComponent",  //this is a struct? do users usually set this?
      //"labelComponent",  //this is a struct? do users usually set this?
      "labels",
      "name",
      "origin",  //not usually set manually
      "sortKey",
      "sortOrder",
      "standalone",
      "style",
      "theme",
      "x",
      "y",
      "y0",
    ]

    const renderSubPlot = () => {
      if (chart_type === 'bar') {
        const barPropsList = commonProps.concat(["alignment", "barRatio", "barWidth", "cornerRadius"]);
        return <VictoryBar {..._.pick(this.props.args, barPropsList)} />
      } else {
        const scatterPropsList = commonProps.concat(["symbol", "size"])
        return <VictoryScatter {..._.pick(this.props.args, scatterPropsList)} />
      }
    }

    const renderPlot = () => {
      if (chart_type === 'pie') {
        const piePropsList = commonProps.concat(["radius", "startAngle", "endAngle"]);
        return <VictoryPie  {..._.pick(this.props.args, piePropsList)} />
      } else {
        return (
          <VictoryChart {..._.pick(this.props.args, chartPropList)}>
            {renderSubPlot()}
          </VictoryChart>
        )
      }
    }

    return renderPlot();

  }
}

// "withStreamlitConnection" is a wrapper function. It bootstraps the
// connection between your component and the Streamlit app, and handles
// passing arguments from Python -> Component.
//
// You don't need to edit withStreamlitConnection (but you're welcome to!).
export default withStreamlitConnection(MyComponent)
