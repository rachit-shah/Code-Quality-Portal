$(window).load(function(){

    // Check if private is checked and show "Access Token" field accordingly
    toggleAccessTokenField();
    $("#private").change(function(){
        toggleAccessTokenField();

    });

});

// Function to toggle visibility of "Access Token" field
function toggleAccessTokenField() {
    if($("#private").is(':checked')){
        $("#access-token-div").show();
    }else{
        $("#access-token-div").hide();
    }
}