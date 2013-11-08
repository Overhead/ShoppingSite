 $(function() {
     var logDiv = $("#log");
     var $tabs = $("#models-one").tabs({
     selected: null,
     select: function(event, ui) {
        loadTab( ui.index ); // ui.index = index of the clicked tab
            }
        });
     //$( "#tabs li" ).removeClass( "ui-corner-top" ).addClass( "ui-corner-left" );
     $('button').on('click',{value: 'list'}, function(event) {
      //Here I want to reload the current selected tab
      loadTab( event, this.id , this.name);
      logDiv.append("LOG: " + this.id + " name: "+this.name +"<br>")
      return false;
     });

    /*  $('#models').tabs('select',0); */
    });

    function loadTab(event, id,name){
        var divName=name;
     $.ajax({
      type: "GET",
      url: "{{ BASE_URL }}/journal/"+id+"/",
      dataType: "html",
      cntName:name,
      success: function(data,name) {
       var content = "";
/*     $.each(data.items, function(items){
        content += "<a class='add' href='#'>" + this.title + "</a><br>";
       }); */
       $("#Content").html(content + "<br /> "+ this.title+ "Tab Index #" + divName+ " on " + (new Date()).toUTCString());
      },
      error: function(XMLHttpRequest, textStatus, errorThrown) {
       if (!$('#error').length) $("#Content").prepend('<div id="error"></div>');
       $('#error').html(textStatus + '<br />'+divName+'<br />');
      }
     })
    }
  
