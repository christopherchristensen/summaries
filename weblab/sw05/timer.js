document.onreadystatechange = function () {
    if (document.readyState === "complete") {

        var timer = {

            startButton: document.getElementById("control-start"),

            stopButton: document.getElementById("control-stop"),

            resetButton: document.getElementById("control-reset"),

            upMinutesButton: document.getElementById("minutes-up"),

            downMinutesButton: document.getElementById("minutes-down"),

            upSecondsButton: document.getElementById("seconds-up"),

            downSecondsButton: document.getElementById("seconds-down"),

            display: document.getElementById("timer-display").childNodes[1],

            minutes: document.getElementById("timer-display").childNodes[1].innerHTML.split(":")[0],

            seconds: document.getElementById("timer-display").childNodes[1].innerHTML.split(":")[1],

            runningInterval: null,

            countdown: function (element, minutes, seconds){

                var setTime;

                return setTime = setInterval(function(){

                    seconds = Number(seconds) < 10 ? "0"+Number(seconds) : Number(seconds);
                    minutes = Number(minutes) < 10 ? "0"+Number(minutes) : Number(minutes);

                    element.display.innerHTML = minutes + ":" + seconds;

                    element.seconds = seconds--;
                    element.minutes = minutes;

                    if (seconds < 0) {

                        element.minutes = minutes--;
                        element.seconds = seconds = 59;

                        if(minutes < 0) {
                            clearInterval(setTime);
                        }

                    }

                }, 1000);

            },
            
            stopCountdown: function (interval) {
                clearInterval(interval);
            },
            
            resetTimer: function (element) {
                element.display.innerHTML = "00:00";
                element.minutes = 0;
                element.seconds = 0;


                if(element.runningInterval) {
                    element.stopCountdown(element.runningInterval);
                    element.runningInterval = null;
                }
            }

        }

        timer.startButton.addEventListener("click", function () {

            if(!timer.runningInterval) {

                timer.runningInterval = timer.countdown(

                    timer, timer.minutes, timer.seconds

                );

            }

        });
        
        timer.stopButton.addEventListener("click", function () {

            timer.stopCountdown(timer.runningInterval);
            timer.runningInterval = null;

        });
        
        timer.resetButton.addEventListener("click", function () {

            timer.resetTimer(timer);

        });
        
        timer.upMinutesButton.addEventListener("click", function () {

            timer.minutes = Number(timer.minutes) + 1;

            if(timer.minutes < 10) {
                timer.minutes = "0" + Number(timer.minutes);
            }
            if(timer.seconds < 10) {
                timer.seconds = "0" + Number(timer.seconds);
            }

            timer.display.innerHTML = timer.minutes + ":" + timer.seconds;

        });
        
        timer.downMinutesButton.addEventListener("click", function () {

            if(Number(timer.minutes) != 0) {

                timer.minutes = Number(timer.minutes) - 1;

                if(timer.minutes < 10) {
                    timer.minutes = "0" + timer.minutes;
                }
                if(Number(timer.seconds) < 10) {
                    timer.seconds = "0" + Number(timer.seconds);
                }
                timer.display.innerHTML = timer.minutes + ":" + timer.seconds;

            }

        });
        
        timer.upSecondsButton.addEventListener("click", function () {

            timer.seconds = Number(timer.seconds) + 1;

            if(timer.seconds > 59) {
                timer.minutes = Number(timer.minutes) + 1;
                timer.seconds = "00";
            }

            if(Number(timer.minutes) < 10) {
                timer.minutes = "0" + Number(timer.minutes);
            }
            if(timer.seconds < 10 && timer.seconds != "00") {
                timer.seconds = "0" + timer.seconds;
            }

            timer.display.innerHTML = timer.minutes + ":" + timer.seconds;

        });
        
        timer.downSecondsButton.addEventListener("click", function () {

            if(Number(timer.minutes) + Number(timer.seconds) != 0) {

                timer.seconds = Number(timer.seconds) - 1;

                if(timer.seconds < 0) {
                    if(Number(timer.minutes) != 0) {
                        timer.minutes = Number(timer.minutes) - 1;
                        timer.seconds = "59";
                    }
                }

                if(Number(timer.minutes) < 10) {
                    timer.minutes = "0" + Number(timer.minutes);
                }
                if(timer.seconds < 10) {
                    timer.seconds = "0" + timer.seconds;
                }

                timer.display.innerHTML = timer.minutes + ":" + timer.seconds;

            }

        });

    }

}

