$(document).ready(function(){

	$('#sina-tv-play').click(function() {

		$('#sina-tv-content').html("");
		$('#sina-tv-content').append('<IFRAME id="sina-tv" style="height: 400px; width: 100%" src="http://sports.sina.com.cn/tv" ></IFRAME>');
	});

	$('#sina-tv-stop').click(function() {

		$('#sina-tv-content').html("");
		$('#sina-tv-content').append('<h3 class="text-primary">新浪体育直播</h3>' +
										'<hr>' +
										'<dl>' +
        									'<dt>打开直播台</dt>' +
       	 										'<dd>点击右上角的' +
       	 										'<label class="btn btn-default btn-xs"><i class="fa fa-play"></i></label>按钮，打开直播台' +
       	 										'</dd>' +
        									'<dt>关闭直播台</dt>' +
        										'<dd>点击右上角的' +
        										'<label class="btn btn-default btn-xs"><i class="fa fa-stop"></i></label>按钮，关闭直播台' +
        										'</dd>' +
      									'</dl>');
	});

	$('#sina-video-play').click(function() {

		$('#sina-video-content').html("");
		$('#sina-video-content').append('<IFRAME id="sina-video" marginwidth="0" marginheight="0" scrolling="no" style="POSITION: absolute; TOP: -100px;height: 400px; width: 100%" src="http://sports.sina.com.cn/nba/video/" ></IFRAME>');
	});

	$('#sina-video-stop').click(function() {

		$('#sina-video-content').html("");
		$('#sina-video-content').append('<h3 class="text-primary">每日焦点视频</h3>' +
										'<hr>' +
										'<dl>' +
        									'<dt>观看视频</dt>' +
       	 										'<dd>点击右上角的' +
       	 										'<label class="btn btn-default btn-xs"><i class="fa fa-play"></i></label>按钮，观看视频' +
       	 										'</dd>' +
        									'<dt>关闭视频</dt>' +
        										'<dd>点击右上角的' +
        										'<label class="btn btn-default btn-xs"><i class="fa fa-stop"></i></label>按钮，关闭视频' +
        										'</dd>' +
      									'</dl>');
	});

	$('.hupuTopicRefresh').click(function(){

		$.ajax({

        	type: "GET",
       		url: "/api-auth/hupu/topic",
        
       		beforeSend: function() {

       			$(".hupuTopicRefresh").html('<h5><i class="icon-spinner icon-spin blue"></i></h5>');
       		},
       		
       		success: function(data) {

       			$("#topicContent").html("");

       			$(".hupuTopicRefresh").html('<a href="##" data-action="reload" class="hupuTopicRefresh">' +
								'<i class="icon-refresh blue"></i>' +
								'</a>');

           		for(var i = 0; i < Number(data.count); i++) {

           		var html = '<div class="profile-activity clearfix">' +
										'<div>' +
											'<img class="pull-left" src="/static/ace/assets/avatars/avatar4.png" />' +
											'<div class="red">' +
											'<b>' + data.results[i].reply + '</b>' +
											'</div>' +
											'<div class="text"><a href="' + data.results[i].titleLink + '" target="_blank">' + data.results[i].title + '</a></div>' +
										'</div>' +
									'</div>';

					$("#topicContent").append(html);
				}

       		}
		});
	});

	$('.hupuTodayRefresh').click(function(){

		$.ajax({

        	type: "GET",
       		url: "/api-auth/hupu/today",
        
       		beforeSend: function() {

       			$(".hupuTodayRefresh").html('<h5><i class="icon-spinner icon-spin blue"></i></h5>');
       		},
       		
       		success: function(data) {

       			$("#todayContent").html("");

       			$(".hupuTodayRefresh").html('<a href="##" data-action="reload" class="hupuTodayRefresh">' +
								'<i class="icon-refresh blue"></i>' +
								'</a>');

           		for(var i = 0; i < Number(data.count); i++) {

           		var html = '<div class="widget-body">' +
						'<div class="widget-main padding-8">' +
						'	<div class="profile-feed">' +
						'		<div class="profile-activity clearfix">' +
						'			<div>' +
						'				<div class="row-fluid">' +
						'					<div class="span2">' +
						'					<div class="pull-right">' +
						'					<span class="' + data.results[i].teamlogo1 + '"></span>' +
						'					</div>' +
						'					</div>' +
						'					<div class="span8">' +
						'					<center>' +
						'					<a class="user" href="' + data.results[i].titleLink + '" target="_blank"> ' + data.results[i].title + ' </a>' +
						'					</center>' +
						'					</div>' +
						'					<div class="span2">' +
						'					<div class="pull-left">' +
						'					<span class="' + data.results[i].teamlogo2 + '"></span>' +
						'					</div>' +
						'					</div>' +
						'				</div>	' +
						'				<div class="time">' +
						'					<center>' +
						'					<i class="icon-time bigger-110"></i>' +
						'					<a href="' + data.results[i].alertLink + '"" target="_blank">' +
						'					' + data.results[i].alert + '' +
						'					</a>' +
						'					</center>' +
						'				</div>' +
						'			</div>' +
						'		</div>' +

								
						'	</div>' +
						'</div>' +
						'</div>';

					$("#todayContent").append(html);
				}

       		}
		});
	});
});