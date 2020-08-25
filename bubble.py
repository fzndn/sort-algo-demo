from manimlib.imports import *

class Demo(Scene):
	CONFIG = {
		'box_color' : BLUE_C,
		'pointer_color' : PINK,
	}


	def construct(self):
		self.showArray()
		self.doSort()

	def doSort(self):
		array = self.array
		array.generate_target()
		array.target.shift(UP)

		self.play(MoveToTarget(array))

		self.pointer = RegularPolygon(3,start_angle=-PI/2, color=self.pointer_color, fill_opacity=1).scale(0.2).next_to(self.boxes[0], UP)

		self.play(ShowCreation(self.pointer))

		self._comparison_1()
		self._comparison_2()
		self._comparison_3()
		self._comparison_4()
		self._comparison_5()
		self._comparison_6()
		self._comparison_7()
		self._comparison_8()
		self._comparison_9()
		self._comparison_10()

		self.play(FadeOut(self.pointer))

		self._activateArray()

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

	def showArray(self):
		boxes = []

		for i in range(10):
			boxes.append(
				Square(side_length=1.0, color=self.box_color).move_to(4.5 * LEFT + i * RIGHT)
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

	def _comparison_10(self):
		self._resetPointer()

		self._deactivateBox(self.boxes[0], self.num_0)

	def _comparison_9(self):
		self._resetPointer()

		self._noSwap(self.boxes[0], self.boxes[1], "0", "1")

		self._deactivateBox(self.boxes[1], self.num_1)

	def _comparison_8(self):
		self._resetPointer()

		self._noSwap(self.boxes[0], self.boxes[1], "0", "1")
		self._noSwap(self.boxes[1], self.boxes[2], "1", "2")

		self._deactivateBox(self.boxes[2], self.num_2)

	def _comparison_7(self):
		self._resetPointer()

		self._noSwap(self.boxes[0], self.boxes[1], "0", "1")
		self._noSwap(self.boxes[1], self.boxes[2], "1", "2")
		self._noSwap(self.boxes[2], self.boxes[3], "2", "3")

		self._deactivateBox(self.boxes[3], self.num_3)

	def _comparison_6(self):
		self._resetPointer()

		self._noSwap(self.boxes[0], self.boxes[1], "0", "1")
		self._noSwap(self.boxes[1], self.boxes[2], "1", "2")
		self._noSwap(self.boxes[2], self.boxes[3], "2", "3")
		self._noSwap(self.boxes[3], self.boxes[4], "3", "4")

		self._deactivateBox(self.boxes[4], self.num_4)

	def _comparison_5(self):
		self._resetPointer()

		self._swap(  self.boxes[0], self.boxes[1], "1", "0", self.num_1, self.num_0)
		self._noSwap(self.boxes[1], self.boxes[2], "1", "3")
		self._swap(  self.boxes[2], self.boxes[3], "3", "2", self.num_3, self.num_2)
		self._noSwap(self.boxes[3], self.boxes[4], "3", "4")
		self._noSwap(self.boxes[4], self.boxes[5], "4", "5")

		self._deactivateBox(self.boxes[5], self.num_5)

	def _comparison_4(self):
		self._resetPointer()

		self._noSwap(self.boxes[0], self.boxes[1], "1", "3")
		self._swap(  self.boxes[1], self.boxes[2], "3", "0", self.num_3, self.num_0)
		self._noSwap(self.boxes[2], self.boxes[3], "3", "4")
		self._swap(  self.boxes[3], self.boxes[4], "4", "2", self.num_4, self.num_2)
		self._noSwap(self.boxes[4], self.boxes[5], "4", "5")
		self._noSwap(self.boxes[5], self.boxes[6], "5", "6")

		self._deactivateBox(self.boxes[6], self.num_6)

	def _comparison_3(self):
		self._resetPointer()

		self._swap(  self.boxes[0], self.boxes[1], "3", "1", self.num_3, self.num_1)
		self._noSwap(self.boxes[1], self.boxes[2], "3", "4")
		self._swap(  self.boxes[2], self.boxes[3], "4", "0", self.num_4, self.num_0)
		self._noSwap(self.boxes[3], self.boxes[4], "4", "5")
		self._swap(  self.boxes[4], self.boxes[5], "5", "2", self.num_5, self.num_2)
		self._noSwap(self.boxes[5], self.boxes[6], "5", "6")
		self._noSwap(self.boxes[6], self.boxes[7], "6", "7")

		self._deactivateBox(self.boxes[7], self.num_7)

	def _comparison_2(self):
		self._resetPointer()

		self._noSwap(self.boxes[0], self.boxes[1], "3", "4")
		self._swap(  self.boxes[1], self.boxes[2], "4", "1", self.num_4, self.num_1)
		self._noSwap(self.boxes[2], self.boxes[3], "4", "7")
		self._swap(  self.boxes[3], self.boxes[4], "7", "0", self.num_7, self.num_0)
		self._swap(  self.boxes[4], self.boxes[5], "7", "5", self.num_7, self.num_5)
		self._swap(  self.boxes[5], self.boxes[6], "7", "2", self.num_7, self.num_2)
		self._swap(  self.boxes[6], self.boxes[7], "7", "6", self.num_7, self.num_6)
		self._noSwap(self.boxes[7], self.boxes[8], "7", "8")

		self._deactivateBox(self.boxes[8], self.num_8)

	def _comparison_1(self):
		self._noSwap(self.boxes[0], self.boxes[1], "3", "4")
		self._noSwap(self.boxes[1], self.boxes[2], "4", "9")
		self._swap(  self.boxes[2], self.boxes[3], "9", "1", self.num_9, self.num_1)
		self._swap(  self.boxes[3], self.boxes[4], "9", "7", self.num_9, self.num_7)
		self._swap(  self.boxes[4], self.boxes[5], "9", "0", self.num_9, self.num_0)
		self._swap(  self.boxes[5], self.boxes[6], "9", "5", self.num_9, self.num_5)
		self._swap(  self.boxes[6], self.boxes[7], "9", "2", self.num_9, self.num_2)
		self._swap(  self.boxes[7], self.boxes[8], "9", "6", self.num_9, self.num_6)
		self._swap(  self.boxes[8], self.boxes[9], "9", "8", self.num_9, self.num_8)

		self._deactivateBox(self.boxes[9], self.num_9)

	def _noSwap(self, left_box, right_box, left_value, right_value):
		highlight = VGroup(left_box, right_box)
		brace = Brace(highlight, DOWN)
		brace_text = TexMobject(left_value + " \\leq " + right_value).next_to(brace, DOWN)

		self.play(
			AnimationGroup(
				GrowFromCenter(brace),
				Write(brace_text),
				lag_ratio=0.2
			)
		)
		self.play(
			FadeOut(brace),
			FadeOut(brace_text),
		)

		self._shiftPointer()

	def _swap(self, left_box, right_box, left_value, right_value, left_num, right_num):
		highlight = VGroup(left_box, right_box)
		brace = Brace(highlight, DOWN)
		brace_text = TexMobject(left_value + "\\text{ }\\textgreater\\text{ }" + right_value).next_to(brace, DOWN)
		result = TextMobject("Swap").move_to(2 * DOWN)

		self.play(
			AnimationGroup(
				GrowFromCenter(brace),
				Write(brace_text),
				lag_ratio=0.2
			)
		)
		self.play(
			FadeIn(result)
		)
		self.play(Swap(left_num, right_num))
		self.play(
			FadeOut(brace),
			FadeOut(brace_text),
			FadeOut(result),
		)

		self._shiftPointer()

	def _deactivateBox(self, box, num):
		self.play(
			FadeToColor(box, GREY),
			FadeToColor(num, GREY),
		)

	def _activateArray(self):
		self.play(
			AnimationGroup(
				FadeToColor(self.boxes[0], self.box_color),
				FadeToColor(self.num_0, WHITE),
				FadeToColor(self.boxes[1], self.box_color),
				FadeToColor(self.num_1, WHITE),
				FadeToColor(self.boxes[2], self.box_color),
				FadeToColor(self.num_2, WHITE),
				FadeToColor(self.boxes[3], self.box_color),
				FadeToColor(self.num_3, WHITE),
				FadeToColor(self.boxes[4], self.box_color),
				FadeToColor(self.num_4, WHITE),
				FadeToColor(self.boxes[5], self.box_color),
				FadeToColor(self.num_5, WHITE),
				FadeToColor(self.boxes[6], self.box_color),
				FadeToColor(self.num_6, WHITE),
				FadeToColor(self.boxes[7], self.box_color),
				FadeToColor(self.num_7, WHITE),
				FadeToColor(self.boxes[8], self.box_color),
				FadeToColor(self.num_8, WHITE),
				FadeToColor(self.boxes[9], self.box_color),
				FadeToColor(self.num_9, WHITE),
				lag_ratio=0.1
			)
		)

	def _shiftPointer(self):
		self.pointer.generate_target()
		self.pointer.target.shift(RIGHT)
		self.play(MoveToTarget(self.pointer))

	def _resetPointer(self):
		self.pointer.generate_target()
		self.pointer.target.next_to(self.boxes[0], UP)
		self.play(MoveToTarget(self.pointer))		
