import json
import streamlit as st
import streamlit.components.v1 as components

def render_map(country_colors):
    html_content = """
    <script src="https://www.amcharts.com/lib/4/core.js"></script>
    <script src="https://www.amcharts.com/lib/4/maps.js"></script>
    <script src="https://www.amcharts.com/lib/4/geodata/worldLow.js"></script>
    <script src="https://www.amcharts.com/lib/4/themes/animated.js"></script>
    <div id="chartdiv" style="width: 100%; height: 500px;"></div>
    <script>
    // Themes begin
    am4core.useTheme(am4themes_animated);
    var chart = am4core.create("chartdiv", am4maps.MapChart);
    chart.geodata = am4geodata_worldLow;
    chart.projection = new am4maps.projections.Orthographic();
    chart.panBehavior = "rotateLongLat";
    chart.deltaLatitude = -20;
    chart.padding(20,20,20,20);

    var countryColors = JSON.parse('""" + json.dumps(country_colors) + """');

    var polygonSeries = chart.series.push(new am4maps.MapPolygonSeries());
    polygonSeries.useGeodata = true;

    // Configure series
    var polygonTemplate = polygonSeries.mapPolygons.template;
    polygonTemplate.tooltipText = "{name}";
    polygonTemplate.stroke = am4core.color("#454a58");
    polygonTemplate.strokeWidth = 0.5;

    // Assign colors to countries
    polygonSeries.data = countryColors.map(function(item) {
        return { id: item.countryCode, fill: am4core.color(item.color) };
    });

    </script>
    """
    components.html(html_content, height=600)