;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname translate-shape) (read-case-sensitive #t) (teachpacks ((lib "convert.rkt" "teachpack" "htdp") (lib "guess.rkt" "teachpack" "htdp") (lib "master.rkt" "teachpack" "htdp") (lib "hangman.rkt" "teachpack" "htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "convert.rkt" "teachpack" "htdp") (lib "guess.rkt" "teachpack" "htdp") (lib "master.rkt" "teachpack" "htdp") (lib "hangman.rkt" "teachpack" "htdp")) #f)))
;;定义圆和矩形
(define-struct circle (posn banjin color))
(define-struct trangle (posn lang width color))
;;定义draw-shap函数
(define (draw-shape shape)
  (cond
    [(circle? shape) (draw-circle (circle-posn shape) (circle-banjin shape) (circle-color shape))]
    [(trangle? shape) (draw-solid-rect (trangle-posn shape) (trangle-lang shape) (trangle-width shape) (trangle-color shape))]))
;;定义translate-shap函数
(define (translate-shape shape delta)
  (cond
    [(circle? shape) (make-circle (make-posn (+ (posn-x (circle-posn shape)) delta) (posn-y (circle-posn shape))) (circle-banjin shape) (circle-color shape))]
    [(trangle? shape) (make-trangle (make-posn (+ (posn-x (trangle-posn shape)) delta) (posn-y (trangle-posn shape))) (trangle-lang shape) (trangle-width shape) (trangle-color shape))]))
;;定义clear-shap函数
(define (clear-shape shape)
  (cond
    [(circle? shape) (clear-circle (circle-posn shape) (circle-banjin shape) (circle-color shape))]
    [(trangle? shape) (clear-solid-rect (trangle-posn shape) (trangle-lang shape) (trangle-width shape) (trangle-color shape))]))
;;定义draw-and-clear函数
(define (draw-and-clear shape)
  (and (and (draw-shape shape) (sleep-for-a-while 1)) (clear-shape shape)))
;;定义主函数
(define (move-shape shape delta)
  (cond
    [(draw-and-clear shape) (translate-shape shape delta)]
    [else shape]))
;;执行
(start 200 100)
(define a-shape (make-trangle (make-posn 20 20) 20 10 'red))
(define a-delta 10)
(draw-shape
 (move-shape
  (move-shape
   (move-shape
    (move-shape a-shape a-delta) a-delta) a-delta) a-delta))
