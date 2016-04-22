$(document).ready(function(){
	$("#createform").submit(function(event){
		var todoTemplate = '<div class = "row"><div class="small-6 large-4 columns"><h2 class="title"><a href="/posts/edit/{{slug}}">{{title}}</a></h2><p>{{content}}</p><p>created at: {{created_at}}</p><p>author:{{user}}</p></div></div><br>';
		function addPost(post){

			$('#allposts').prepend(Mustache.render(todoTemplate, post));
			console.log(post)
		}
		//prevents default settings
		event.preventDefault();
		
		var form = $(this);
		var url = form.attr("action");
		console.log(url);
		var post = $.post(url,$(this).serialize(), function(data){
			addPost(data);
		});
		console.log(post);
	// $.get(url, function(post){
 //        JSON.parse(post.responseText);
 //        console.log(post);
 //    })
  })

	$('#createbutton').on('click',function(event){
		event.preventDefault();

		var button = $(this);
		var url = button.attr('href');
		console.log(url);

		$.get(url,function (){
			Mustache.render(url);
		});
	})
});

