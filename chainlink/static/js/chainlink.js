/**
 * Created with PyCharm.
 * User: seemless
 * Date: 1/25/13
 * Time: 4:30 PM
 * To change this template use File | Settings | File Templates.
 */

var chainlink = function(){

    var revCounts = [50,40,30,20,10,5];
    var debug = false;
    var keyword;
    var currentNumLinks = 50;
    //var host = '50.116.22.120';
    //var port = '5000';

    //Private
    function setKeyword(word){
        keyword = word;
        //$('#linkTitle').html(keyword);
    };

    function setNumLinks(num){
        $('#numLinks').html(num);
    };

    function setTest(val){
        debug = val;
    }

    function submitKeyword(){
        var newKeyword = $('#keyword').val();
        setKeyword(newKeyword);
        update(50);
    }

    function moreLinks(){
        if(currentNumLinks >= 50){
            update(50);
        }
        else{
            currentNumLinks += 10;
            update(currentNumLinks);
        }
    }

    function fewerLinks(){
        if(currentNumLinks <= 10){
            update(10);
        }
        else{
            currentNumLinks -= 10;
            update(currentNumLinks);
        }
    }

    function update(numLinks){
        var serviceLink = '';


        if(debug){
            serviceLink += "/searchTest"
        }
        else{
            serviceLink += "http://127.0.0.1:5000/search/"+keyword+"/"+numLinks;
        }

        $.getJSON(serviceLink, function(data, text, obj){
            if(data){

                //currData = data;
                $("#wordcloud").html("");

                var htmlStr = '';
                var words = data['words'];

                for(var key in words){
                    if(words.hasOwnProperty(key)){
                        var span = $(document.createElement('span'))
                            .attr({'data-weight': words[key],
                                    'style':'display: none;',
                                    'onclick': "console.log('"+key+"')"

                                    })
                            .html(key)
                            ;
                        $('#wordcloud').append(span);

                    }
                }
                //console.log('produced this html:' +htmlStr.toString());

                $('#wordcloud').awesomeCloud({
                    size: { normalize: true },
                    shape: "circle",
                    font: "Helvetica, Arial, Sans",
                    options: {
                        color: "random-light",
                        rotationRatio: 0,
                        sort: "highest"
                    }
                });

                //setNumLinks(numLinks);

            }
        });


    };


    function reset(){
        revCounts = [50,40,30,20,10,5];
    };

    function getNextCount(){
        return revCounts.pop();
    };

    return {
        reset: reset,
        update: update,
        setNumLinks: setNumLinks,
        getNextCount: getNextCount,
        setDebug: setTest,
        submitKeyword: submitKeyword,
        fewerLinks: fewerLinks,
        moreLinks: moreLinks,
        setKeyword: setKeyword
    };

}();
