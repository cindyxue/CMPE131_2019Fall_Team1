google.load('visualization', '1.0', { packages:["timeline"] });
google.setOnLoadCallback(start);

/*
VARIABLES PASSED FROM managerviewsch.html:
schedule_starts: String array of format 'HH:MM'
schedule_ends: String array of format 'HH:MM'
schedule_days: String array of format 'YYYY-MM-DD'
employee_names: String array
ALL VARIABLES PASSED SHOULD BE ARRAYS OF THE SAME LENGTH 
*/

function start() {
  var timelineHolder = document.getElementById("schedule-graph");
  var timeline = new google.visualization.Timeline(timelineHolder);
  var dataTable = prepareDataTable();

  timeline.draw(dataTable);
}

function prepareDataTable() {
  var dataTable = new google.visualization.DataTable();

  // Add columns
  dataTable.addColumn({ type: 'string', id: 'Name'});
  dataTable.addColumn({ type: 'string', id: 'dummy bar label'}); // necessary to use tooltips
  dataTable.addColumn({ type: 'string', role: 'tooltip' });
  dataTable.addColumn({ type: 'date', id: 'Start'});
  dataTable.addColumn({ type: 'date', id: 'End'});

  // Add Rows 
  
  var rows = []

  for (i = 0; i < schedule_starts.length; i++) {
    var start_time = schedule_starts[i].split(":");
    var end_time = schedule_ends[i].split(":");
    var dates = schedule_days[i].split("-");
    /*
    Intended tooltip format:
    Day - MM/DD
    Start time - HH:MM
    End time - HH:MM
    */
    var tooltip = 'Day - ' + dates[1] + "/" + dates[2];
    tooltip += "Start time - " + start_time[0] + ":" + start_time[1];
    tooltip += "\n";
    tooltip += "End time - " + start_time[0] + ":" + start_time[1];

    // Row Format: ['Name on left', null, 'tooltip', Start (Date object), End (Date object)]
    // Date object format: (year, month, day, hours, minutes)
    start_date_obj = new Date(dates[0], dates[1], dates[2], start_time[0], start_time[1])
    end_date_obj = new Date(dates[0], dates[1], dates[2], start_time[0], start_time[1], 0)
    rows.push([employee_names[i], null, tooltip, start_date_obj, end_date_obj])

  }

  dataTable.addRows([

    /*
    // Format to follow: ['Name on left', 'Text on bar', 'Start date', 'End date']
    // Date format: (year, month, day, hours, minutes, seconds)
*/
    [ 'Chris Williams',  'Butcher',    new Date(0,0,0,12,0,0),  new Date(0,0,0,14,0,0) ],
    [ 'Chris Williams',  'Butcher',    new Date(0,0,0,14,30,0), new Date(0,0,0,16,0,0) ],
    [ 'Chris Williams',  'Cashier', new Date(0,0,0,16,30,0), new Date(0,0,0,19,0,0) ],
    [ 'Thomas Jefferson', 'Cashier',   new Date(0,0,0,12,30,0), new Date(0,0,0,14,0,0) ],
    [ 'Thomas Jefferson', 'Cashier',       new Date(0,0,0,14,30,0), new Date(0,0,0,16,0,0) ],
    [ 'Thomas Jefferson', 'Shelf stocker',        new Date(0,0,0,16,30,0), new Date(0,0,0,18,0,0) ],
    [ 'Jake Anderson',   'Security',       new Date(0,0,0,12,30,0), new Date(0,0,0,14,0,0) ],
    [ 'Jake Anderson',   'Security',             new Date(0,0,0,14,30,0), new Date(0,0,0,16,0,0) ],
    [ 'Jake Anderson',   'Deli',          new Date(0,0,0,16,30,0), new Date(0,0,0,18,30,0) ]]);
    
  
  return dataTable;
}