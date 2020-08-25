from manimlib.imports import *

class Demo(Scene):
	def construct(self):
		self.showArray()
		self.doSort()

	def showArray(self):
		boxes = []

		for i in range(10):
			boxes.append(
				Square(side_length=1.0, color=BLUE_C).move_to(4.5 * LEFT + i * RIGHT)
			)

		self.boxes = boxes

		array_boxes = VGroup(*boxes)

		self.num_3 = TextMobject("3").move_to(4.5 * LEFT)
		self.num_4 = TextMobject("4").move_to(3.5 * LEFT)
		self.num_9 = TextMobject("9").move_to(2.5 * LEFT)
		self.num_1 = TextMobject("1").move_to(1.5 * LEFT)
		self.num_7 = TextMobject("7").move_to(0.5 * LEFT)
		self.num_0 = TextMobject("0").move_to(0.5 * RIGHT)
		self.num_5 = TextMobject("5").move_to(1.5 * RIGHT)
		self.num_2 = TextMobject("2").move_to(2.5 * RIGHT)
		self.num_6 = TextMobject("6").move_to(3.5 * RIGHT)
		self.num_8 = TextMobject("8").move_to(4.5 * RIGHT)

		self.play(
			AnimationGroup(
				ShowCreation(boxes[0]), 
				ShowCreation(boxes[1]),
				ShowCreation(boxes[2]),
				ShowCreation(boxes[3]),
				ShowCreation(boxes[4]),
				ShowCreation(boxes[5]),
				ShowCreation(boxes[6]),
				ShowCreation(boxes[7]),
				ShowCreation(boxes[8]),
				ShowCreation(boxes[9]),
				lag_ratio=0.2
			),
		)

		self.play(
			AnimationGroup(
				Write(self.num_0),
				Write(self.num_1),
				Write(self.num_2),
				Write(self.num_3),
				Write(self.num_4),
				Write(self.num_5),
				Write(self.num_6),
				Write(self.num_7),
				Write(self.num_8),
				Write(self.num_9),
				lag_ratio=0.2
			),
		)

		self.array = VGroup(array_boxes,
			self.num_0, self.num_1, self.num_2, self.num_3, self.num_4, self.num_5, self.num_6, self.num_7, self.num_8, self.num_9)

		brace = Brace(self.array, DOWN)
		brace_text = brace.get_text("array A")

		self.play(
			GrowFromCenter(brace),
			Write(brace_text),
		)

		self.wait()

		self.play(
			FadeOut(brace),
			FadeOut(brace_text),
		)

	def doSort(self):
		array = self.array
		array.generate_target()
		array.target.shift(UP)

		self.play(MoveToTarget(array))

		key_box = Square(side_length=1.0, color=BLUE_C).move_to(4.5 * RIGHT + 2 * DOWN)
		key_text = TextMobject("Key").next_to(key_box, UP)

		self.pointer_num = RegularPolygon(3,start_angle=-PI/2, color=PINK, fill_opacity=1).scale(0.2).next_to(self.boxes[0], UP)
		self.pointer_key = RegularPolygon(3,start_angle= PI/2, color=PINK, fill_opacity=1).scale(0.2).next_to(self.boxes[1], DOWN)

		self.play(
			ShowCreation(key_box),
			Write(key_text),
		)
		self.play(ShowCreation(self.pointer_key))

		self.key_box = key_box

		self._comparison_1()
		self._comparison_2()
		self._comparison_3()
		self._comparison_4()
		self._comparison_5()
		self._comparison_6()
		self._comparison_7()
		self._comparison_8()
		self._comparison_9()

		self.play(
			FadeOut(key_box),
			FadeOut(key_text),
			FadeOut(self.pointer_key)
		)

		array.generate_target()
		array.target.shift(DOWN)

		self.play(MoveToTarget(array))

		ordered = TextMobject("Sorted").move_to(UP)

		self.play(Write(ordered))

		self.wait(3)

		self.play(
			FadeOut(array),
			FadeOut(ordered),
		)

		self.wait(10)

	def _comparison_1(self):
		self._storeKey(self.num_4, "4")
		self._keyGreaterThan("3")

		self._restoreKey(self.num_4, self.boxes[1])

	def _comparison_2(self):
		self._resetPointer(2)

		self._storeKey(self.num_9, "9")
		self._keyGreaterThan("4")

		self._restoreKey(self.num_9, self.boxes[2])

	def _comparison_3(self):
		self._resetPointer(3)

		self._storeKey(self.num_1, "1")
		self._keyLessThan("9", self.num_9)
		self._shiftPointerNum()
		self._keyLessThan("4", self.num_4)
		self._shiftPointerNum()
		self._keyLessThan("3", self.num_3)

		self._restoreKey(self.num_1, self.boxes[0])

	def _comparison_4(self):
		self._resetPointer(4)

		self._storeKey(self.num_7, "7")
		self._keyLessThan("9", self.num_9)
		self._shiftPointerNum()
		self._keyGreaterThan("4")

		self._restoreKey(self.num_7, self.boxes[3])

	def _comparison_5(self):
		self._resetPointer(5)

		self._storeKey(self.num_0, "0")
		self._keyLessThan("9", self.num_9)
		self._shiftPointerNum()
		self._keyLessThan("7", self.num_7)
		self._shiftPointerNum()
		self._keyLessThan("4", self.num_4)
		self._shiftPointerNum()
		self._keyLessThan("3", self.num_3)
		self._shiftPointerNum()
		self._keyLessThan("1", self.num_1)

		self._restoreKey(self.num_0, self.boxes[0])

	def _comparison_6(self):
		self._resetPointer(6)

		self._storeKey(self.num_5, "5")
		self._keyLessThan("9", self.num_9)
		self._shiftPointerNum()
		self._keyLessThan("7", self.num_7)
		self._shiftPointerNum()
		self._keyGreaterThan("4")

		self._restoreKey(self.num_5, self.boxes[4])

	def _comparison_7(self):
		self._resetPointer(7)

		self._storeKey(self.num_2, "2")
		self._keyLessThan("9", self.num_9)
		self._shiftPointerNum()
		self._keyLessThan("7", self.num_7)
		self._shiftPointerNum()
		self._keyLessThan("5", self.num_5)
		self._shiftPointerNum()
		self._keyLessThan("4", self.num_4)
		self._shiftPointerNum()
		self._keyLessThan("3", self.num_3)
		self._shiftPointerNum()
		self._keyGreaterThan("1")

		self._restoreKey(self.num_2, self.boxes[2])

	def _comparison_8(self):
		self._resetPointer(8)

		self._storeKey(self.num_6, "6")
		self._keyLessThan("9", self.num_9)
		self._shiftPointerNum()
		self._keyLessThan("7", self.num_7)
		self._shiftPointerNum()
		self._keyGreaterThan("5")

		self._restoreKey(self.num_6, self.boxes[6])

	def _comparison_9(self):
		self._resetPointer(9)

		self._storeKey(self.num_8, "8")
		self._keyLessThan("9", self.num_9)
		self._shiftPointerNum()
		self._keyGreaterThan("7")

		self._restoreKey(self.num_8, self.boxes[8])

	def _keyLessThan(self, value, num):
		point_text = TexMobject("\\text{Key }" + "\\textless" + "\\text{ }" + value).next_to(self.pointer_num, UP)
		result = TextMobject("Shift " + value).move_to(2 * DOWN)
		num.generate_target()
		num.target.shift(RIGHT)

		self.play(Write(point_text))
		self.play(Write(result))
		self.play(MoveToTarget(num))
		self.play(
			FadeOut(point_text),
			FadeOut(result),
		)

	def _resetPointer(self, index):
		self.pointer_key.generate_target()
		self.pointer_key.target.next_to(self.boxes[index], DOWN)
		self.pointer_num.next_to(self.boxes[index - 1], UP)

		self.play(MoveToTarget(self.pointer_key))

	def _shiftPointerNum(self):
		self.pointer_num.generate_target()
		self.pointer_num.target.shift(LEFT)
		self.play(MoveToTarget(self.pointer_num))

	def _restoreKey(self, key, box):
		key.generate_target()
		key.target.move_to(box.get_center())
		result = TextMobject("Restore Key").move_to(2 * DOWN)

		self.play(FadeOut(self.pointer_num))
		self.play(Write(result))
		self.play(MoveToTarget(key))
		self.play(FadeOut(result))

	def _keyGreaterThan(self, num):
		point_text = TexMobject("\\text{Key }" + "\\geq" + "\\text{ }" + num).next_to(self.pointer_num, UP)
		result = TextMobject("Stop").move_to(2 * DOWN)

		self.play(Write(point_text))
		self.play(Write(result))
		self.play(
			FadeOut(point_text),
			FadeOut(result),
		)

	def _storeKey(self, num, value):
		num.generate_target()
		num.target.move_to(self.key_box)
		result = TextMobject("Store " + value + " as Key").move_to(2 * DOWN)

		self.play(Write(result))
		self.play(MoveToTarget(num))
		self.play(FadeOut(result))
		self.play(ShowCreation(self.pointer_num))