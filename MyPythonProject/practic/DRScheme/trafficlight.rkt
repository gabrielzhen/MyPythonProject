;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname trafficlight) (read-case-sensitive #t) (teachpacks ((lib "convert.rkt" "teachpack" "htdp") (lib "guess.rkt" "teachpack" "htdp") (lib "master.rkt" "teachpack" "htdp") (lib "draw.rkt" "teachpack" "htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "convert.rkt" "teachpack" "htdp") (lib "guess.rkt" "teachpack" "htdp") (lib "master.rkt" "teachpack" "htdp") (lib "draw.rkt" "teachpack" "htdp")) #f)))
;;红绿灯大小
(define width 50)
(define height 160)
(define bulb-radius 20)
(define bulb-distance 10)

;;灯泡位置
(define x-bulbs (quotient width 2))
(define y-red (+ bulb-distance  bulb-radius))
(define y-yellow (+ y-red bulb-distance (* 2 bulb-radius)))
(define y-green (+ y-yellow bulb-distance (* 2 bulb-radius)))

;;绘制
(define (y-color color)
  (cond
  [(symbol=? color 'red) y-red]
  [(symbol=? color 'yellow) y-yellow]
  [(symbol=? color 'green) y-green]))

(define (clearcircle color)
  (clear-circle (make-posn x-bulbs (y-color color)) bulb-radius color))

(define (clearbulb color)
  (clear-solid-disk (make-posn x-bulbs (y-color color)) bulb-radius color))

(define (drawcircle color)
  (draw-circle (make-posn x-bulbs (y-color color)) bulb-radius color))
(define (drawbulb color)
  (draw-solid-disk (make-posn x-bulbs (y-color color)) bulb-radius color))

(define (clear-bulb color)
  (and (clearbulb color) (drawcircle color)))

(define (switch color1 color2)
  (and (clear-bulb color1) (drawbulb color2)))

(define (next curr-color)
  (cond
    [(and (symbol=? curr-color 'red) (switch 'red 'green)) 'green]
    [(and (symbol=? curr-color 'yellow) (switch 'yellow 'red)) 'red]
    [(and (symbol=? curr-color 'green) (switch 'green 'yellow)) 'yellow]
    ))


(start width height)
(drawbulb 'red)
(sleep-for-a-while 3)
(next 'red)
(sleep-for-a-while 3)
(next 'green)
(sleep-for-a-while 3)
(next 'yellow)
