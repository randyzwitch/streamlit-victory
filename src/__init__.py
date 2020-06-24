import os
import streamlit as st

# Create a _RELEASE constant. We'll set this to False while we're developing
# the component, and True when we're ready to package and distribute it.
_RELEASE = False

# Declare a Streamlit component
if not _RELEASE:
    _component_func = st.declare_component(
        # We give the component a simple, descriptive name ("my_component"
        # does not fit this bill, so please choose something better for your
        # own component :)
        "VictoryChart",
        # Pass `url` here to tell Streamlit that the component will be served
        # by the local dev server that you run via `npm run start`.
        # (This is useful while your component is in development.)
        url="http://localhost:3001",
    )
else:
    # When we're distributing a production version of the component, we'll
    # replace the `url` param with `path`, and point it to to the component's
    # build directory:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = st.declare_component("VictoryChart", path=build_dir)


def victory_bar(data, x, y, key=None, **kwargs):

    """Create a bar chart.

    Parameters
    ----------

    data: [dict]
        A list of dicts representing data row-wise

    x: str
        Key name of independent variable

    y: str
        Key name of dependent variable

    key: str or None
        An optional key that uniquely identifies this component. If this is
        None, and the component's arguments are changed, the component will
        be re-mounted in the Streamlit frontend and lose its current state.

    Returns
    -------
    None
    """

    return _component_func(chart_type="bar", data=data, x=x, y=y, key=key, **kwargs)


def victory_pie(data, x, y, key=None, **kwargs):

    """Create a pie chart.

    Parameters
    ----------

    data: [dict]
        A list of dicts representing data row-wise

    x: str
        Key name of independent variable

    y: str
        Key name of dependent variable

    key: str or None
        An optional key that uniquely identifies this component. If this is
        None, and the component's arguments are changed, the component will
        be re-mounted in the Streamlit frontend and lose its current state.

    Returns
    -------
    None
    """

    return _component_func(chart_type="pie", data=data, x=x, y=y, key=key, **kwargs)


def victory_scatter(data, x, y, key=None, **kwargs):

    """Create a scatter plot.

    Parameters
    ----------

    data: [dict]
        A list of dicts representing data row-wise

    x: str
        Key name of independent variable

    y: str
        Key name of dependent variable

    key: str or None
        An optional key that uniquely identifies this component. If this is
        None, and the component's arguments are changed, the component will
        be re-mounted in the Streamlit frontend and lose its current state.
    
    Returns
    -------
    None
    """

    return _component_func(chart_type="scatter", data=data, x=x, y=y, key=key, **kwargs)


# Add some test code to play with the component while it's in development.
# During development, we can run this just as we would any other Streamlit
# app: `$ streamlit run my_component/__init__.py`
if not _RELEASE:

    data = [
        {"quarter": "1", "earnings": 13000},
        {"quarter": "2", "earnings": 16500},
        {"quarter": "3", "earnings": 14250},
        {"quarter": "4", "earnings": 19000},
    ]

    bar_chart = victory_bar(
        data,
        "quarter",
        "earnings",
        alignment="start",
        animate=False,
        width=500,
        horizontal=True,
        barWidth=None,
        barRatio=0.2,
        sortKey=None,
        sortOrder=None,
        scale=None,
    )

    pie_chart = victory_pie(data, "quarter", "earnings",)

    scatter_chart = victory_scatter(data, "quarter", "earnings",)
