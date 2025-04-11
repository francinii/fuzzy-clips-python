(deftemplate Temperature
  0 40
  ((cold (0 1) (10 0))
   (warm (5 0) (20 1) (30 0))
   (hot (25 0) (40 1) (40 1))))

(deftemplate Humidity
  0 100
  ((low (0 1) (20 0))
   (medium (10 0) (50 1) (90 0))
   (high (70 0) (100 1) (100 1))))

(deftemplate FanSpeed
  0 100
  ((slow (0 1) (30 0))
   (medium (20 0) (50 1) (80 0))
   (fast (60 0) (100 1) (100 1))))

(defrule cool-fan
  (Temperature cold)
  (Humidity low)
 =>
  (assert (FanSpeed slow)))

(defrule moderate-fan
  (Temperature warm)
  (Humidity medium)
 =>
  (assert (FanSpeed medium)))

(defrule hot-humid-fan
  (Temperature hot)
  (Humidity high)
 =>
  (assert (FanSpeed fast)))

(defrule backup-fan
  (Temperature ?t)
  (Humidity ?h)
  (not (FanSpeed ?)) ; si no se ha definido aún FanSpeed
 =>
  (assert (FanSpeed medium)))

(deffacts sample-facts
  (Temperature (5 0) (5 1) (5 0))
  (Humidity (10 0) (10 1) (10 0)))
