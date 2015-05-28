
/* Twitter Bootstrap Tooltip
 *
 * Link Tooltips
/*====================================================================*/
$(function() {
	$('[rel="tooltip"]').tooltip({
		placement : 'top'
	});
	$('#table-todo').selectRow({
		classname : 'line'
	});
});

/* Datatable
 *
 * dashboard datatable sample
/*====================================================================*/
$(function () {
	$('#table1').dataTable({
		"bProcessing": true,
		"sAjaxSource": "js/jquery.datatable.arrays.txt"
	});
});
$(function () {
	$("#spark1").sparkline([5,6,7,9,9,5,3,2,2,4,6,7], {
		type: 'line',
		type: 'line',
		width: '100',
		height: '30',
		lineWidth: 3,
		spotRadius: 3,
		lineColor: '#bf0000',
		fillColor: '#ffaaaa',
		spotColor: '#7f007f',
		minSpotColor: '#ffaaff',
		maxSpotColor: '#ff00ff',
		highlightSpotColor: '#0000ff',
		highlightLineColor: '#7f003f',
		drawNormalOnTop: true
   });
   $("#spark2").sparkline([5,6,7,-5,1,-3,-2,4,5,2,7,3,1], {
		type: 'bar',
		height: '30',
		barWidth: 7,
		barSpacing: 1,
		negBarColor: '#ff5656'
   });
});