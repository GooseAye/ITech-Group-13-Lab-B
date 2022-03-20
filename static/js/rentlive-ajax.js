/* TWD pg 301 */

$(document).ready(function(){
	$('.FollowButton').click(function(){
		var propertyNameVar;
		propertyNameVar = $(this).attr('data-categoryid');

		$.get('/rentlive/follow_property',
			{'name': propertyNameVar},
			function(data){
				$('#FollowerCount').html("Followers: " + data);
				$('.FollowButton').hide();
				$('.FollowMessage').html("You have followed this property!");
			})
	})

	$('.LikeButton').click(function(){
		var commentID;
		commentID = $(this).attr('data-categoryid');

		$.get('/rentlive/likecomment/',
			{'commentID': commentID},
			function(data){
				$('#likes').html("Likes: " + data);
				$('.LikeButton').hide();
				$('.likemessage').html("You have liked this comment");
			})
	})

	$('.AgentLikeButton').click(function(){
		var commentID;
		commentID = $(this).attr('data-categoryid')

		$.get('/rentlive/likeagentcomment/',
			{'commentID': commentID},
			function(data){
				$('#agentLikes').html("Likes: " + data);
				$('.AgentLikeButton').hide();
				$('#Agentlikemessage').html("You have liked this comment");
			})
	})

/* TWD pg 309 */
	$('#QuickSearch').keyup(function(){
		var query;
		query = $(this).val();
		$.get('/rentlive/suggestion/',
			{'suggestion': query},
			function(data){
				$('#CitySearch').html(data);
			})
	});

	$('#Followed').click(function(){
		var user;
		user = $(this).attr('data-categoryid');
		$('#ProfileContent').empty();
		$.get('/rentlive/follows/',
			function(data){
				$('#ProfileContent').html(data);
			})
	});

	$('#MyMessage').click(function(){
		var user;
		user = $(this).attr('data-categoryid')
		$('#ProfileContent').empty();
		$.get('/rentlive/showmessages/',
			function(data){
				$('#ProfileContent').html(data);
			})
	})

	$('#MyComments').click(function(){
		$.get('/rentlive/showcomments',
			function(data){
				$('#ProfileContent').html(data);
			})
	})

	$('#CommentButton').click(function(){
		var user;
		user=$(this).attr('data-categoryid')
		$.get('/rentlive/addcomment/',
			function(data){
				$('#commentform').html(data);
			})
	})

	$('#AgentComment').click(function(){
		var user;
		user=$(this).attr('data-categoryid')
		$.get('/rentlive/agentcomment/',
			function(data){
				$('#AgCommentForm').html(data);
			})
	})

	$('#Message').click(function(){
		$('#ProfileContent').empty();
	})

	$('#Comments').click(function(){
		$('#ProfileContent').empty();
	})

	$('#SendMessage').click(function(){
		$('#ProfileContent').empty();
		$.get('/rentlive/message/',
			function(data){
				$('#ProfileContent').html(data);
			})
	})

	$('#MessageSending').click(function(){
		$('#ProfileContent').empty();
		$.get('/rentlive/sent/',
			function(data){
				$('#ProfileContent').html(data);
			})
	})


});