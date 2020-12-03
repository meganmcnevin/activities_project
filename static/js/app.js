"use strict";


/* STARS ANIMATION   */

$('input[type="radio"]').click(function() {
  var thisNumber = $(this).attr('id').slice(-1);
  $(this).siblings('label').each(function() {
    var starSib = $(this).attr('for').slice(-1);
    if (starSib <= thisNumber) {
      $(this).addClass('on');
    } else {
      $(this).removeClass('on');
    }
  });
});

/* ADVANCED SEARCH  */


$(document).ready(function() { 
  // alert("Value of hidden field before updating: " 
  //                       + $("#hiddenField").val()); 
  
            $("#mainSearch").on('submit', (evt) => { 
                $("#hiddenField").val($("#textSearch").val()).trigger("change"); 
                evt.preventDefault();
                $("#results").empty();
                submitForm()
            }); 
  
            $("#hiddenField").change(function() { 
                // alert("Value of hidden field after updating: " 
                //         + $("#hiddenField").val()); 
                      }); 
      });


window.addEventListener('load', (evt) => {
  evt.preventDefault();
  $("#results").empty();
  submitForm();
});

$("#myform").on('submit', (evt) => {
  evt.preventDefault();
  $("#results").empty();
  submitForm();
});
  
function submitForm() {
  var form = document.myform; 
  var dataString = $(form).serialize(); 
    
    $.get('/filter', dataString, (response) =>{

      var names = []; 
      $.each(response.activities, function(idx, val) {
          names.push("<div class='search-card mb-3'><div class='row no-gutters'><div class='col-md-3'><img class='card-img' src=" + val.activity_description['overview']['photo'] + "></div>" +"<div class='col-md-9'> <div class='card-header'><a href="+ "/activity/"+ val.activity_id + "><h5>" + val.activity_name + "</h5></a></div><h5 class='card-title'></h5><p class='card-text'>" + val.activity_description['overview']['Overview'] +  val.keywords +"</p></div></div></div></div>" );
          
          console.log(names); 
          
          });
          $.each(names, function(idx, value) {
            $("#results").append(value);
          });
    });
  }; 

    $(document).ready(function() {
      $('#effort').multiselect({
          enableFiltering: true,
          filterBehavior: 'value'
      });
  });

  $(document).ready(function() {
    $('#material').multiselect({
        enableFiltering: true,
        filterBehavior: 'text',
        checkboxName: function (option) {
          return 'materials[]';
        }
    });
});

$(document).ready(function() {
  $('#interest').multiselect({
      enableFiltering: true,
      filterBehavior: 'text',
      checkboxName: function (option) {
        return 'interests[]';
      }
  });
});


$(document).ready(function() {
  $('#addinterest').multiselect({
      enableFiltering: true,
      filterBehavior: 'text',
      checkboxName: function (option) {
        return 'interests[]';
      }
  });
});



$(document).ready(function() {
  $('#time_period').multiselect({
      enableFiltering: true,
      filterBehavior: 'text',
      checkboxName: function (option) {
        return 'time_periods[]';
      }
  });
});


/* FAVORITE ANIMATION  */

$(document).ready(function(){
  $("#heart").click(function(){
    if($("#heart").hasClass("liked")){
      $("#heart").removeClass("liked");
    }else{
      $("#heart").addClass("liked");
    }
  });
});




// $(document).ready(function() {
//   if ($(activity in user.activities;
//   $("#heart").addClass("liked");

// })
