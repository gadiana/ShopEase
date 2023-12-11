$(document).ready(function() {
	$('#butlogin1').on('click', function() {

		var username = $('#username').val();
		var password = $('#password').val();
		if(username!="" && password!="" ){
			$.ajax({
				url: "processfolder/process.php",
				type: "POST",
				data: {
					type:2,
					username: username,
					password: password						
				},
				cache: false,
				success: function(dataResult){

					var dataResult = JSON.parse(dataResult);

					if(dataResult.result==1){
						location.href = "index.php";	
                        				
					}

					else{
                        alert("Please register!");
					}

					
				}
			});
		}else{
			alert('Please fill all the field !');
		}
	});


    
    // setInterval(function() {
    //     var today = new Date();
    //     var tomorrow = new Date(today);
    //     tomorrow.setDate(today.getDate() + 1);
    //     var yr = tomorrow.getFullYear();
    //     var mn = (tomorrow.getMonth() + 1).toString().padStart(2, '0');
    //     var dy = tomorrow.getDate().toString().padStart(2, '0');
    //     var final_date = yr + "-" + mn + "-" + dy;
    
    //     $.ajax({
    //         url: "/yourapp/check_tomorrow/",  // Update this URL to match your Django app name
    //         type: "POST",
    //         data: {
    //             check_tomm: 1,
    //             date_tomorrow: final_date
    //         },
    //         cache: false,
    //         success: function(dataResult) {
    //             var dataResult_1 = JSON.parse(dataResult);
    //             if (dataResult_1.yes === 1) {
    //                 alert("Hey " + dataResult_1.name + ", You have a Cart to buy tomorrow! Please go and check it");
    //             }
    //         }
    //     });
    
    // }, 1000);

     
});
$('#logout').on('click', function() {

    $.ajax({
            url: "processfolder/process.php",
            type: "POST",
            data: {
                type:3					
            },
            cache: false,
            success: function(dataResult){

                var dataResult = JSON.parse(dataResult);

                if(dataResult.result==2){
                    location.href = "index.php";	
                                    
                }
                
            }
    });
});


// MODAL SCRIPT

document.addEventListener("DOMContentLoaded", function () {
    // Get the modal and buttons
    var modal = document.getElementById("modal");
    var openModalBtn = document.getElementById("openModalBtn");
    var closeModalBtn = document.getElementById("closeModalBtn");

    // Open the modal
    openModalBtn.onclick = function () {
        modal.style.display = "block";
    }

    // Close the modal
    closeModalBtn.onclick = function () {
        modal.style.display = "none";
    }

    // Close the modal if the user clicks outside of it
    window.onclick = function (event) {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    }
});
//Manage Modal Script
document.addEventListener("DOMContentLoaded", function () {
    // Get the modal and buttons
    var modal = document.getElementById("modalManage");
    var openModalBtn = document.getElementById("openModalBtnManage");
    var closeModalBtn = document.getElementById("closeModalBtnManage");

    // Open the modal
    openModalBtn.onclick = function () {
        modal.style.display = "block";
    }

    // Close the modal
    closeModalBtn.onclick = function () {
        modal.style.display = "none";
    }

    // Close the modal if the user clicks outside of it
    window.onclick = function (event) {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    }
});
//Open cart Modal 
document.addEventListener("DOMContentLoaded", function () {
    // Get the modal and buttons
    var modal = document.getElementById("modalOpenCart");
    var openModalBtn = document.getElementById("openModalOpenCart");
    var closeModalBtn = document.getElementById("closeModalOpenCart");

    // Open the modal
    openModalBtn.onclick = function () {
        modal.style.display = "block";
    }

    // Close the modal
    closeModalBtn.onclick = function () {
        modal.style.display = "none";
    }

    // Close the modal if the user clicks outside of it
    window.onclick = function (event) {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    }
});

function showSuccessPopup() {
    alert("Cart updated successfully!");
}