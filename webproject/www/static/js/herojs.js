function getweapon() {
    var pagestatus = $.ajax({
        url: '/weapon',
        dataType: 'json',
        success: function (data) {
        
        },
        error: function (data) {
            alert(data.status);
        }
    });
}