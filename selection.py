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

		triangle_min = RegularPolygon(3,start_angle=-PI/2, color=PINK, fill_opacity=1).scale(0.2).next_to(self.boxes[0], UP)
		min_text = TextMobject("min").next_to(triangle_min, UP)
		self.min = VGroup(triangle_min, min_text)

		triangle_i = RegularPolygon(3,start_angle=-PI/2, color=PINK, fill_opacity=1).scale(0.2).next_to(self.boxes[0], UP)
		i_text = TexMobject("i").next_to(triangle_i, UP, buff=0.75)
		self.i_point = VGroup(triangle_i, i_text)

		triangle_j = RegularPolygon(3,start_angle=-PI/2, color=PINK, fill_opacity=1).scale(0.2).next_to(self.boxes[1], UP)
		j_text = TexMobject("j").next_to(triangle_j, UP, buff=0.75)
		self.j_point = VGroup(triangle_j, j_text)

		self.play(ShowCreation(self.i_point))
		self.play(ShowCreation(self.min))
		self.play(ShowCreation(self.j_point))

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

		self.play(FadeOut(self.i_point))

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

	def _comparison_1(self):
		self._lessThan(   self.boxes[0], self.boxes[1], "3", "4")
		self._shiftJ()
		self._lessThan(   self.boxes[0], self.boxes[2], "3", "9")
		self._shiftJ()
		self._greaterThan(self.boxes[0], self.boxes[3], "3", "1")
		self._shiftJ()
		self._lessThan(   self.boxes[3], self.boxes[4], "1", "7")
		self._shiftJ()
		self._greaterThan(self.boxes[3], self.boxes[5], "1", "0")
		self._shiftJ()
		self._lessThan(   self.boxes[5], self.boxes[6], "0", "5")
		self._shiftJ()
		self._lessThan(   self.boxes[5], self.boxes[7], "0", "2")
		self._shiftJ()
		self._lessThan(   self.boxes[5], self.boxes[8], "0", "6")
		self._shiftJ()
		self._lessThan(   self.boxes[5], self.boxes[9], "0", "8")

		self._comparisonDone(self.boxes[0], self.num_3, self.num_0, "3", "0")

	def _comparison_2(self):
		self._shiftI()
		self._resetMinJ(1)

		self._lessThan(   self.boxes[1], self.boxes[2], "4", "9")
		self._shiftJ()
		self._greaterThan(self.boxes[1], self.boxes[3], "4", "1")
		self._shiftJ()
		self._lessThan(   self.boxes[3], self.boxes[4], "1", "7")
		self._shiftJ()
		self._lessThan(   self.boxes[3], self.boxes[5], "1", "3")
		self._shiftJ()
		self._lessThan(   self.boxes[3], self.boxes[6], "1", "5")
		self._shiftJ()
		self._lessThan(   self.boxes[3], self.boxes[7], "1", "2")
		self._shiftJ()
		self._lessThan(   self.boxes[3], self.boxes[8], "1", "6")
		self._shiftJ()
		self._lessThan(   self.boxes[3], self.boxes[9], "1", "8")

		self._comparisonDone(self.boxes[1], self.num_4, self.num_1, "4", "1")

	def _comparison_3(self):
		self._shiftI()
		self._resetMinJ(2)

		self._greaterThan(self.boxes[2], self.boxes[3], "9", "4")
		self._shiftJ()
		self._lessThan(   self.boxes[3], self.boxes[4], "4", "7")
		self._shiftJ()
		self._greaterThan(self.boxes[3], self.boxes[5], "4", "3")
		self._shiftJ()
		self._lessThan(   self.boxes[5], self.boxes[6], "3", "5")
		self._shiftJ()
		self._greaterThan(self.boxes[5], self.boxes[7], "3", "2")
		self._shiftJ()
		self._lessThan(   self.boxes[7], self.boxes[8], "2", "6")
		self._shiftJ()
		self._lessThan(   self.boxes[7], self.boxes[9], "2", "8")

		self._comparisonDone(self.boxes[2], self.num_9, self.num_2, "9", "2")

	def _comparison_4(self):
		self._shiftI()
		self._resetMinJ(3)

		self._lessThan(   self.boxes[3], self.boxes[4], "4", "7")
		self._shiftJ()
		self._greaterThan(self.boxes[3], self.boxes[5], "4", "3")
		self._shiftJ()
		self._lessThan(   self.boxes[5], self.boxes[6], "3", "5")
		self._shiftJ()
		self._lessThan(   self.boxes[5], self.boxes[7], "3", "9")
		self._shiftJ()
		self._lessThan(   self.boxes[5], self.boxes[8], "3", "6")
		self._shiftJ()
		self._lessThan(   self.boxes[5], self.boxes[9], "3", "8")

		self._comparisonDone(self.boxes[3], self.num_4, self.num_3, "4", "3")	

	def _comparison_5(self):
		self._shiftI()
		self._resetMinJ(4)

		self._greaterThan(self.boxes[4], self.boxes[5], "7", "4")
		self._shiftJ()
		self._lessThan(   self.boxes[5], self.boxes[6], "4", "5")
		self._shiftJ()
		self._lessThan(   self.boxes[5], self.boxes[7], "4", "9")
		self._shiftJ()
		self._lessThan(   self.boxes[5], self.boxes[8], "4", "6")
		self._shiftJ()
		self._lessThan(   self.boxes[5], self.boxes[9], "4", "8")

		self._comparisonDone(self.boxes[4], self.num_7, self.num_4, "7", "4")

	def _comparison_6(self):
		self._shiftI()
		self._resetMinJ(5)

		self._greaterThan(self.boxes[5], self.boxes[6], "7", "5")
		self._shiftJ()
		self._lessThan(   self.boxes[6], self.boxes[7], "5", "9")
		self._shiftJ()
		self._lessThan(   self.boxes[6], self.boxes[8], "5", "6")
		self._shiftJ()
		self._lessThan(   self.boxes[6], self.boxes[9], "5", "8")

		self._comparisonDone(self.boxes[5], self.num_7, self.num_5, "7", "5")

	def _comparison_7(self):
		self._shiftI()
		self._resetMinJ(6)

		self._lessThan(   self.boxes[6], self.boxes[7], "7", "9")
		self._shiftJ()
		self._greaterThan(self.boxes[6], self.boxes[8], "7", "6")
		self._shiftJ()
		self._lessThan(   self.boxes[8], self.boxes[9], "6", "8")
		
		self._comparisonDone(self.boxes[6], self.num_7, self.num_6, "7", "6")

	def _comparison_8(self):
		self._shiftI()
		self._resetMinJ(7)

		self._greaterThan(self.boxes[7], self.boxes[8], "9", "7")
		self._shiftJ()
		self._lessThan(   self.boxes[8], self.boxes[9], "7", "8")

		self._comparisonDone(self.boxes[7], self.num_9, self.num_7, "9", "7")

	def _comparison_9(self):
		self._shiftI()
		self._resetMinJ(8)

		self._greaterThan(self.boxes[8], self.boxes[9], "9", "8")

		self._comparisonDone(self.boxes[8], self.num_9, self.num_8, "9", "8")

	def _comparison_10(self):
		self._shiftI()
		self._deactivateBox(self.boxes[9], self.num_9)

	def _comparisonDone(self, left_most_box, left_most_num, min_num, left_value, right_value):
		self._swap(left_most_num, min_num, left_value, right_value)
		self.play(
			FadeOut(self.min),
			FadeOut(self.j_point),
		)
		self._deactivateBox(left_most_box, min_num)

	def _lessThan(self, left_box, right_box, left_value, right_value):
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

	def _greaterThan(self, left_box, right_box, left_value, right_value):
		highlight = VGroup(left_box, right_box)
		brace = Brace(highlight, DOWN)
		brace_text = TexMobject(left_value + "\\text{ }\\textgreater\\text{ }" + right_value).next_to(brace, DOWN)
		result = TexMobject("\\text{Move min to }" + "j").move_to(2 * DOWN)

		self.play(
			AnimationGroup(
				GrowFromCenter(brace),
				Write(brace_text),
				lag_ratio=0.2
			)
		)
		self.play(FadeIn(result))
		self._moveMin(right_box)
		self.play(
			FadeOut(brace),
			FadeOut(brace_text),
			FadeOut(result),
		)

	def _moveMin(self, box):
		self.min.generate_target()
		self.min.target.next_to(box, UP)
		self.play(MoveToTarget(self.min))

	def _shiftI(self):
		self.i_point.generate_target()
		self.i_point.target.shift(RIGHT)
		self.play(MoveToTarget(self.i_point))

	def _shiftJ(self):
		self.j_point.generate_target()
		self.j_point.target.shift(RIGHT)
		self.play(MoveToTarget(self.j_point))

	def _swap(self, left_num, right_num, left_value, right_value):
		result = TexMobject("\\text{Swap }" + left_value + "\\text{ with }" + right_value).move_to(2 * DOWN)
		self.play(FadeIn(result))
		self.play(Swap(left_num, right_num))
		self.play(FadeOut(result))

	def _deactivateBox(self, box, num):
		self.play(
			FadeToColor(box, GREY),
			FadeToColor(num, GREY),
		)

	def _resetMinJ(self, index):
		self.min.next_to(self.boxes[index], UP)
		self.j_point.next_to(self.boxes[index + 1], UP)

		self.play(ShowCreation(self.min))
		self.play(ShowCreation(self.j_point))

	def _activateArray(self):
		self.play(
			AnimationGroup(
				FadeToColor(self.boxes[0], BLUE_C),
				FadeToColor(self.num_0, WHITE),
				FadeToColor(self.boxes[1], BLUE_C),
				FadeToColor(self.num_1, WHITE),
				FadeToColor(self.boxes[2], BLUE_C),
				FadeToColor(self.num_2, WHITE),
				FadeToColor(self.boxes[3], BLUE_C),
				FadeToColor(self.num_3, WHITE),
				FadeToColor(self.boxes[4], BLUE_C),
				FadeToColor(self.num_4, WHITE),
				FadeToColor(self.boxes[5], BLUE_C),
				FadeToColor(self.num_5, WHITE),
				FadeToColor(self.boxes[6], BLUE_C),
				FadeToColor(self.num_6, WHITE),
				FadeToColor(self.boxes[7], BLUE_C),
				FadeToColor(self.num_7, WHITE),
				FadeToColor(self.boxes[8], BLUE_C),
				FadeToColor(self.num_8, WHITE),
				FadeToColor(self.boxes[9], BLUE_C),
				FadeToColor(self.num_9, WHITE),
				lag_ratio=0.05
			)
		)