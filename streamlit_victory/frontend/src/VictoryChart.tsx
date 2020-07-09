import React, { ReactNode } from "react"
import {
  withStreamlitConnection,
  StreamlitComponentBase,
  // Streamlit,
} from "./streamlit"
import {
  VictoryArea,
  VictoryBar,
  VictoryChart,
  VictoryLine,
  VictoryPie,
  VictoryScatter,
  VictoryTheme,
  VictoryBoxPlot,
  VictoryHistogram,
} from 'victory'
import _ from 'lodash'

/**
 * This is a React-based component template. The `render()` function is called
 * automatically when your component should be re-rendered.
 */
class STVictoryChart extends StreamlitComponentBase {

  public render = (): ReactNode => {

    // Arguments that are passed to the plugin in Python are accessible
    // via `this.props.args`.
    const chart_type = this.props.args["chart_type"]

    const theme = this.props.args["theme"] === "material" ? VictoryTheme.material : VictoryTheme.grayscale

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
      "colorScale",
      "containerComponent",
      "cornerRadius",
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

        const barPropsList = commonProps.concat(["alignment", "barRatio", "barWidth"]);
        return <VictoryBar {..._.pick(this.props.args, barPropsList)} />

      } else if (chart_type === 'scatter') {

        const scatterPropsList = commonProps.concat(["maxBubbleSize", "minBubbleSize", "size", "symbol"])
        return <VictoryScatter {..._.pick(this.props.args, scatterPropsList)} />

      } else if (chart_type === 'area') {

        const areaPropsList = commonProps.concat(["interpolation"])
        return <VictoryArea {..._.pick(this.props.args, areaPropsList)} />

      } else if (chart_type === 'line') {

        const linePropsList = commonProps.concat(["interpolation"])
        return <VictoryLine {..._.pick(this.props.args, linePropsList)} />

      } else if (chart_type === 'box') {

        const boxPropsList = commonProps.concat(["boxWidth", "whiskerWidth"])
        return <VictoryBoxPlot {..._.pick(this.props.args, boxPropsList)} />

      } else if (chart_type === 'histogram') {

        const histPropsList = commonProps.concat([])
        return <VictoryHistogram {..._.pick(this.props.args, histPropsList)} />

      }
    }

    const renderPlot = () => {
      if (chart_type === 'pie') {

        const piePropsList = commonProps.concat(
          [
            "colorScale",
            "cornerRadius",
            "endAngle",
            "innerRadius",
            "labelPosition",
            "labelRadius",
            "padAngle",
            "radius",
            "startAngle"
          ]
        );
        return <VictoryPie  {..._.pick(this.props.args, piePropsList)} />

      } else {
        return (

          <VictoryChart {..._.pick(this.props.args, chartPropList)} theme={theme}>
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
export default withStreamlitConnection(STVictoryChart)