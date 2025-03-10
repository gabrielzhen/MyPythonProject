;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname test) (read-case-sensitive #t) (teachpacks ((lib "convert.rkt" "teachpack" "htdp") (lib "guess.rkt" "teachpack" "htdp") (lib "master.rkt" "teachpack" "htdp") (lib "draw.rkt" "teachpack" "htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "convert.rkt" "teachpack" "htdp") (lib "guess.rkt" "teachpack" "htdp") (lib "master.rkt" "teachpack" "htdp") (lib "draw.rkt" "teachpack" "htdp")) #f)))
;;红绿灯大小
(define width 50)
(define height 160)
(define bulb-radius 20)
(define bulb-distance 10)

;;灯泡位置
(define x-bulbs (quotient width 2))
(define y-red (+ bulb-distance (* 2 bulb-radius)))

;;绘制
(start width height)
(draw-solid-disk (make-posn x-bulbs y-red) bulb-radius 'red)