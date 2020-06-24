import os
import streamlit as st

# Create a _RELEASE constant. We'll set this to False while we're developing
# the component, and True when we're ready to package and distribute it.
# (This is, of course, optional - there are innumerable ways to manage your
# release process.)
_RELEASE = False

# Declare a Streamlit component. `st.declare_component` returns a function
# that is used to create instances of the component. We're naming this
# function "_component_func", with an underscore prefix, because we don't want
# to expose it directly to users. Instead, we will create a custom wrapper
# function, below, that will serve as our component's public API.

# It's worth noting that this call to `st.declare_component` is the
# *only thing* you need to do to create the binding between Streamlit and
# your component frontend. Everything else we do in this file is simply a
# best practice.

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


# The wrapper allows us to customize
# our component's API: we can pre-process its input args, post-process its
# output value, and add a docstring for users.
# def vchart(chart_type, data, x, y, animate=True, horizontal=None, key=None):
#     """Create a new instance of "vchart".

#     Parameters
#     ----------

#     chart_type: str
#         A string indicating "bar" or something else

#     data: [dict]
#         A list of dicts representing data row-wise

#     x: str
#         Key name of independent variable

#     y: str
#         Key name of dependent variable

#     animate: bool
#         Animate chart on load

#     horizontal: bool or None
#         Animate chart on load

#     key: str or None
#         An optional key that uniquely identifies this component. If this is
#         None, and the component's arguments are changed, the component will
#         be re-mounted in the Streamlit frontend and lose its current state.

#     Returns
#     -------
#     None

#     """
#     # sent to the frontend, where they'll be available in "args" dictionary
#     component_value = _component_func(
#         chart_type=chart_type, data=data, x=x, y=y, animate=animate, key=key
#     )

#     # We could modify the value returned from the component if we wanted.
#     # There's no need to do this in our simple example - but it's an option.
#     return component_value


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
