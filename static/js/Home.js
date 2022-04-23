function kospi_display(data){
    Highcharts.chart('p_container', {
        chart: {
            zoomType: 'x'
        },
        title: {
            text: '코스피'
        },
        subtitle: {
            text: document.ontouchstart === undefined ?
                'Click and drag in the plot area to zoom in' : 'Pinch the chart to zoom in'
        },
        xAxis: {
            type: 'datetime'
        },
        yAxis: {
            title: {
                text: '체결가'
            }
        },
        legend: {
            enabled: false
        },
        plotOptions: {
            area: {
                fillColor: {
                    linearGradient: {
                        x1: 0,
                        y1: 0,
                        x2: 0,
                        y2: 1
                    },
                    stops: [
                        [0, Highcharts.getOptions().colors[5]],
                        [1, Highcharts.color(Highcharts.getOptions().colors[5]).setOpacity(0).get('rgba')]
                    ]
                },
                marker: {
                    radius: 2
                },
                lineWidth: 1,
                states: {
                    hover: {
                        lineWidth: 1
                    }
                },
                threshold: null
            }
        },
        series: [{
           type: 'area',
           name: '코스피',
           data: data,
           turboThreshold:5000,
        }]
    });
};

function kosdaq_display(data){
    Highcharts.chart('d_container', {
        chart: {
            zoomType: 'x'
        },
        title: {
            text: '코스닥'
        },
        subtitle: {
            text: document.ontouchstart === undefined ?
                'Click and drag in the plot area to zoom in' : 'Pinch the chart to zoom in'
        },
        xAxis: {
            type: 'datetime'
        },
        yAxis: {
            title: {
                text: '체결가'
            }
        },
        legend: {
            enabled: false
        },
        plotOptions: {
            area: {
                fillColor: {
                    linearGradient: {
                        x1: 0,
                        y1: 0,
                        x2: 0,
                        y2: 1
                    },
                    stops: [
                        [0, Highcharts.getOptions().colors[0]],
                        [1, Highcharts.color(Highcharts.getOptions().colors[0]).setOpacity(0).get('rgba')]
                    ]
                },
                marker: {
                    radius: 2
                },
                lineWidth: 1,
                states: {
                    hover: {
                        lineWidth: 1
                    }
                },
                threshold: null
            }
        },
        series: [{
           type: 'area',
           name: '코스닥',
           data: data,
           turboThreshold:5000,
        }]
    });
};

function kospi_getdata(){
    $.ajax({
        url:'kospigraph',
        success:function(data){
            kospi_display(data);
        }
    });
};

function kosdaq_getdata(){
    $.ajax({
        url:'kosdaqgraph',
        success:function(data){
            kosdaq_display(data);
        }
    });
};

function news_getdata(){
    $.ajax({
      url:'main_news_crowling',
      success:function(data){
        main_news_display(data),
        totalData = data.data.length
      }
    });
};

function main_news_display(data){
    var output = '';

    for(var i in data){
        output += '<tr>'
        output += '<td>'
        output += '<a href = "'
        output += data[i].url
        output += '" target = "_blank">'
        output += data[i].title
        output += '</tr>'
        output += '</td>'
        output += '</a>'
    }
//        $('tbody#result').html(output);
    document.getElementById("result").innerHTML = output;
}

$(document).ready(function(){
    news_getdata();
    kospi_getdata();
    kosdaq_getdata();
});