$(function(){

    
    $('#datesubmit').click(function(){
		
		var search_topic = $('#date').val();

        console.log(search_topic)
		
				
		if (search_topic){
                chrome.runtime.sendMessage(
					{topic: search_topic},
					function(response) {
                        // console.log("15")
						result = response.farewell;
						// console.log(result)
						// alert(result.summary);
						
						var notifOptions = {
                            title: "Prediction",
                            iconUrl: "images/icon.png",
							type: "basic",
							message: result.pred + " receipts"
						};
						chrome.notifications.create('WikiNotif1', notifOptions);

                        // var notifOptions = {
                        //     title: "Graph",
                        //     // iconUrl: "http://www.google.com/favicon.ico",
                        //     iconUrl: "images/icon.png",
						// 	type: "basic",
						// 	message: "graph"
						// };
						// chrome.notifications.create('WikiNotif2', notifOptions);


                        console.log(result)
						
					});
		}
			
			
		$('#keyword').val('');
		
    });
});