const endpoint = '/search/'
const delay_by_in_ms = 700
let scheduled_function = false
const search_button=$('search-button');
let search_input=document.getElementById("search-input");

const result_div=document.getElementById("search_result");


let ajax_call = function (endpoint, request_parameters) {
    $.getJSON(endpoint, request_parameters)
        .done(response => {
            console.log(response);
            result_div.innerHTML=response['html_from_view'];
        })
}
document.getElementById("search-button").addEventListener("click",function(e){

    // e.preventDefault();

    console.log(search_input.value);
    const request_parameters = {
        q: search_input.value // value of user_input: the HTML element with ID user-input
    }

    // if scheduled_function is NOT false, cancel the execution of the function
    if (scheduled_function) {
        clearTimeout(scheduled_function)
    }

    // setTimeout returns the ID of the function to be executed
    scheduled_function = setTimeout(ajax_call, delay_by_in_ms, endpoint, request_parameters)


});



