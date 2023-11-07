;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname translate-circle) (read-case-sensitive #t) (teachpacks ((lib "convert.rkt" "teachpack" "htdp") (lib "guess.rkt" "teachpack" "htdp") (lib "master.rkt" "teachpack" "htdp") (lib "draw.rkt" "teachpack" "htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "convert.rkt" "teachpack" "htdp") (lib "guess.rkt" "teachpack" "htdp") (lib "master.rkt" "teachpack" "htdp") (lib "draw.rkt" "teachpack" "htdp")) #f)))
;;定义圆结构体
(define-struct circle (posn banjin color))
;;fun-for-circle circle->???
(define (draw-a-circle a-circle)
  (draw-circle (circle-posn a-circle) (circle-banjin a-circle) (circle-color a-circle)))
;;定义判断一个posn是否在圆圈像素内
(define (in-circle a-circle a-posn)
  (sqrt
   (+ (sqr (- (posn-y (circle-posn a-circle)) (posn-y a-posn)))
      (sqr (- (posn-x (circle-posn a-circle)) (posn-x a-posn)))))
  )
;;定义一个平移一定delta的圆
(define (translate-circle a-circle delta)
  (make-circle (make-posn (+ (posn-x (circle-posn a-circle)) delta) (posn-y (circle-posn a-circle))) (circle-banjin a-circle) (circle-color a-circle)))
;;清除一个圆
(define (clear-a-circle a-circle)
  (clear-circle (circle-posn a-circle) (circle-banjin a-circle) (circle-color a-circle)))
;;画一个圆 过一定时间然后清除
(define (draw-and-clear-circle a-circle)
  (and (and (draw-a-circle a-circle) (sleep-for-a-while 1)) (clear-a-circle a-circle)))
;;在画布上平移
(define (move-circle delta a-circle)
  (cond
    [(draw-and-clear-circle a-circle) (translate-circle a-circle delta)]
    [else a-circle]))
;;start
(start 200 100)
(define a-circle (make-circle (make-posn 20 20) 10 'red))
(draw-a-circle
 (move-circle 10
  (move-circle 10
    (move-circle 10
      (move-circle 10 a-circle)))))

(draw-solid-rect (make-posn 50 50) 10 20 'green)