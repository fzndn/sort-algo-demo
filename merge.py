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

		numbers = []

		for i in range(10):
			numbers.append(
				TextMobject(str(i))
			)

		numbers[3].move_to(boxes[0].get_center())
		numbers[4].move_to(boxes[1].get_center())
		numbers[9].move_to(boxes[2].get_center())
		numbers[1].move_to(boxes[3].get_center())
		numbers[7].move_to(boxes[4].get_center())
		numbers[0].move_to(boxes[5].get_center())
		numbers[5].move_to(boxes[6].get_center())
		numbers[2].move_to(boxes[7].get_center())
		numbers[6].move_to(boxes[8].get_center())
		numbers[8].move_to(boxes[9].get_center())

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
			)
		)

		self.play(
			AnimationGroup(
				Write(numbers[0]),
				Write(numbers[1]),
				Write(numbers[2]),
				Write(numbers[3]),
				Write(numbers[4]),
				Write(numbers[5]),
				Write(numbers[6]),
				Write(numbers[7]),
				Write(numbers[8]),
				Write(numbers[9]),
				lag_ratio=0.2
			)
		)

		self.boxes = boxes
		self.numbers = numbers

		self.array = VGroup(VGroup(*self.boxes), VGroup(*self.numbers))

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

		self.split_pointer = RegularPolygon(3,start_angle= PI/2, color=PINK, fill_opacity=1).scale(0.2)
		self.split_text = TextMobject("Split").next_to(self.split_pointer, DOWN)

		self.left_pointer  = RegularPolygon(3,start_angle=  PI/2, color=PINK, fill_opacity=1).scale(0.2)
		self.right_pointer = RegularPolygon(3,start_angle=  PI/2, color=PINK, fill_opacity=1).scale(0.2)
		self.merge_pointer = RegularPolygon(3,start_angle= -PI/2, color=PINK, fill_opacity=1).scale(0.2)

		self.split_1()

		self.split_2()
		self.split_3()
		self.split_4()
		self.merge_4()
		self.merge_3()
		self.split_6()
		self.merge_6()
		self.merge_2()

		self.split_7()
		self.split_8()
		self.split_9()
		self.merge_9()
		self.merge_8()
		self.split_10()
		self.merge_10()
		self.merge_7()

		self.merge_1()

		array = VGroup(*self.boxes, *self.numbers)
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

	def split_1(self):
		self.showSplitPointer(self.boxes[4], self.boxes[5])

		left_part = VGroup(
			self.boxes[0], self.boxes[1], self.boxes[2], self.boxes[3], self.boxes[4],
			self.numbers[3], self.numbers[4], self.numbers[9], self.numbers[1], self.numbers[7]
		)

		right_part = VGroup(
			self.boxes[5], self.boxes[6], self.boxes[7], self.boxes[8], self.boxes[9],
			self.numbers[0], self.numbers[5], self.numbers[2], self.numbers[6], self.numbers[8]
		)

		self.splitArray(left_part, right_part, 0.3)	

	def split_2(self):
		self.showSplitPointer(self.boxes[2], self.boxes[3])

		left_part = VGroup(
			self.boxes[0], self.boxes[1], self.boxes[2], 
			self.numbers[3], self.numbers[4], self.numbers[9]
		)

		right_part = VGroup(
			self.boxes[3], self.boxes[4],
			self.numbers[1], self.numbers[7]
		)

		self.splitArray(left_part, right_part, 0.2)

	def split_3(self):
		self.showSplitPointer(self.boxes[1], self.boxes[2])

		left_part = VGroup(
			self.boxes[0], self.boxes[1], 
			self.numbers[3], self.numbers[4]
		)

		right_part = VGroup(
			self.boxes[2],
			self.numbers[9]
		)

		self.splitArray(left_part, right_part, 0.1)

	def split_4(self):
		self.showSplitPointer(self.boxes[0], self.boxes[1])

		left_part = VGroup(
			self.boxes[0],
			self.numbers[3]
		)

		right_part = VGroup(
			self.boxes[1], 
			self.numbers[4]
		)

		self.splitArray(left_part, right_part, 0.05)

	def merge_4(self):
		temp_boxes = self.createTempBoxes(2, self.boxes[0], self.boxes[1])

		left_part = VGroup(
			self.boxes[0],
			self.numbers[3]
		)
		left_part.generate_target()
		left_part.target.shift(1.5 * DOWN)

		right_part = VGroup(
			self.boxes[1], 
			self.numbers[4]
		)
		right_part.generate_target()
		right_part.target.shift(1.5 * DOWN)

		self.play(
			AnimationGroup(
				MoveToTarget(left_part),
				MoveToTarget(right_part),
				ShowCreation(temp_boxes[0]),
				ShowCreation(temp_boxes[1]),
				lag_ratio=0.1
			)
		)

		self.showAllPointer(self.boxes[0], self.boxes[1], temp_boxes[0])		
		self.lessThan("3", "4", self.numbers[3], temp_boxes[0])
		self.play(FadeOut(self.left_pointer))
		self.shiftMergePointer()
		self.moveRemaining(self.numbers[4], temp_boxes[1])
		self.play(FadeOut(self.right_pointer))
		self.play(FadeOut(self.merge_pointer), FadeOut(self.boxes[0]), FadeOut(self.boxes[1]))

		self.boxes[0] = temp_boxes[0]
		self.boxes[1] = temp_boxes[1]

		self.play(
			AnimationGroup(
				FadeToColor(self.boxes[0], BLUE_C),
				FadeToColor(self.boxes[1], BLUE_C),
			)
		)

	def merge_3(self):
		temp_boxes = self.createTempBoxes(3, self.boxes[0], self.boxes[2])

		left_part = VGroup(
			self.boxes[0], self.boxes[1],
			self.numbers[3], self.numbers[4]
		)
		left_part.generate_target()
		left_part.target.shift(1.5 * DOWN)

		right_part = VGroup(
			self.boxes[2],
			self.numbers[9]
		)
		right_part.generate_target()
		right_part.target.shift(1.5 * DOWN)

		self.play(
			AnimationGroup(
				MoveToTarget(left_part),
				MoveToTarget(right_part),
				ShowCreation(temp_boxes[0]),
				ShowCreation(temp_boxes[1]),
				ShowCreation(temp_boxes[2]),
				lag_ratio=0.1
			)
		)

		self.showAllPointer(self.boxes[0], self.boxes[2], temp_boxes[0])
		self.lessThan("3", "9", self.numbers[3], temp_boxes[0])
		self.shiftLeftPointer()
		self.shiftMergePointer()
		self.lessThan("4", "9", self.numbers[4], temp_boxes[1])
		self.play(FadeOut(self.left_pointer))
		self.shiftMergePointer()
		self.moveRemaining(self.numbers[9], temp_boxes[2])
		self.play(FadeOut(self.right_pointer))
		self.play(FadeOut(self.merge_pointer), FadeOut(self.boxes[0]), FadeOut(self.boxes[1]), FadeOut(self.boxes[2]))

		self.boxes[0] = temp_boxes[0]
		self.boxes[1] = temp_boxes[1]
		self.boxes[2] = temp_boxes[2]

		self.play(
			AnimationGroup(
				FadeToColor(self.boxes[0], BLUE_C),
				FadeToColor(self.boxes[1], BLUE_C),
				FadeToColor(self.boxes[2], BLUE_C)
			)
		)

	def split_6(self):
		self.showSplitPointer(self.boxes[3], self.boxes[4])

		left_part = VGroup(
			self.boxes[3],
			self.numbers[1]
		)

		right_part = VGroup(
			self.boxes[4], 
			self.numbers[7]
		)

		self.splitArray(left_part, right_part, 0.05)

	def merge_6(self):
		temp_boxes = self.createTempBoxes(2, self.boxes[3], self.boxes[4])

		left_part = VGroup(
			self.boxes[3],
			self.numbers[1]
		)
		left_part.generate_target()
		left_part.target.shift(1.5 * DOWN)

		right_part = VGroup(
			self.boxes[4], 
			self.numbers[7]
		)
		right_part.generate_target()
		right_part.target.shift(1.5 * DOWN)

		self.play(
			AnimationGroup(
				MoveToTarget(left_part),
				MoveToTarget(right_part),
				ShowCreation(temp_boxes[0]),
				ShowCreation(temp_boxes[1]),
				lag_ratio=0.1
			)
		)

		self.showAllPointer(self.boxes[3], self.boxes[4], temp_boxes[0])
		self.lessThan("1", "7", self.numbers[1], temp_boxes[0])
		self.play(FadeOut(self.left_pointer))
		self.shiftMergePointer()
		self.moveRemaining(self.numbers[7], temp_boxes[1])
		self.play(FadeOut(self.right_pointer))
		self.play(FadeOut(self.merge_pointer), FadeOut(self.boxes[3]), FadeOut(self.boxes[4]))

		self.boxes[3] = temp_boxes[0]
		self.boxes[4] = temp_boxes[1]

		self.play(
			AnimationGroup(
				FadeToColor(self.boxes[3], BLUE_C),
				FadeToColor(self.boxes[4], BLUE_C),
			)
		)

	def merge_2(self):
		temp_boxes = self.createTempBoxes(5, self.boxes[0], self.boxes[4])

		left_part = VGroup(
			self.boxes[0], self.boxes[1], self.boxes[2], 
			self.numbers[3], self.numbers[4], self.numbers[9]
		)
		left_part.generate_target()
		left_part.target.shift(1.5 * DOWN)

		right_part = VGroup(
			self.boxes[3], self.boxes[4],
			self.numbers[1], self.numbers[7]
		)
		right_part.generate_target()
		right_part.target.shift(1.5 * DOWN)

		self.play(
			AnimationGroup(
				MoveToTarget(left_part),
				MoveToTarget(right_part),
				ShowCreation(temp_boxes[0]),
				ShowCreation(temp_boxes[1]),
				ShowCreation(temp_boxes[2]),
				ShowCreation(temp_boxes[3]),
				ShowCreation(temp_boxes[4]),
				lag_ratio=0.1
			)
		)

		self.showAllPointer(self.boxes[0], self.boxes[3], temp_boxes[0])
		self.greaterThan("3", "1", self.numbers[1], temp_boxes[0])
		self.shiftRightPointer()
		self.shiftMergePointer()
		self.lessThan("3", "7", self.numbers[3], temp_boxes[1])
		self.shiftLeftPointer()
		self.shiftMergePointer()
		self.lessThan("4", "7", self.numbers[4], temp_boxes[2])
		self.shiftLeftPointer()
		self.shiftMergePointer()
		self.greaterThan("9", "7", self.numbers[7], temp_boxes[3])
		self.play(FadeOut(self.right_pointer))
		self.shiftMergePointer()
		self.moveRemaining(self.numbers[9], temp_boxes[4])
		self.play(FadeOut(self.left_pointer))
		self.play(FadeOut(self.merge_pointer),
			FadeOut(self.boxes[0]), FadeOut(self.boxes[1]), FadeOut(self.boxes[2]), FadeOut(self.boxes[3]), FadeOut(self.boxes[4])
		)

		self.boxes[0] = temp_boxes[0]
		self.boxes[1] = temp_boxes[1]
		self.boxes[2] = temp_boxes[2]
		self.boxes[3] = temp_boxes[3]
		self.boxes[4] = temp_boxes[4]

		self.play(
			AnimationGroup(
				FadeToColor(self.boxes[0], BLUE_C),
				FadeToColor(self.boxes[1], BLUE_C),
				FadeToColor(self.boxes[2], BLUE_C),
				FadeToColor(self.boxes[3], BLUE_C),
				FadeToColor(self.boxes[4], BLUE_C),
			)
		)

	def split_7(self):
		self.showSplitPointer(self.boxes[7], self.boxes[8])

		left_part = VGroup(
			self.boxes[5], self.boxes[6], self.boxes[7],
			self.numbers[0], self.numbers[5], self.numbers[2]
		)

		right_part = VGroup(
			self.boxes[8], self.boxes[9],
			self.numbers[6], self.numbers[8]
		)

		self.splitArray(left_part, right_part, 0.2)

	def split_8(self):
		self.showSplitPointer(self.boxes[6], self.boxes[7])

		left_part = VGroup(
			self.boxes[5], self.boxes[6],
			self.numbers[0], self.numbers[5],
		)

		right_part = VGroup(
			self.boxes[7],
			self.numbers[2],
		)

		self.splitArray(left_part, right_part, 0.1)

	def split_9(self):
		self.showSplitPointer(self.boxes[5], self.boxes[6])

		left_part = VGroup(
			self.boxes[5],
			self.numbers[0]
		)

		right_part = VGroup(
			self.boxes[6],
			self.numbers[5],
		)

		self.splitArray(left_part, right_part, 0.05)

	def merge_9(self):
		temp_boxes = self.createTempBoxes(2, self.boxes[5], self.boxes[6])

		left_part = VGroup(
			self.boxes[5],
			self.numbers[0]
		)
		left_part.generate_target()
		left_part.target.shift(1.5 * DOWN)

		right_part = VGroup(
			self.boxes[6], 
			self.numbers[5]
		)
		right_part.generate_target()
		right_part.target.shift(1.5 * DOWN)

		self.play(
			AnimationGroup(
				MoveToTarget(left_part),
				MoveToTarget(right_part),
				ShowCreation(temp_boxes[0]),
				ShowCreation(temp_boxes[1]),
				lag_ratio=0.1
			)
		)

		self.showAllPointer(self.boxes[5], self.boxes[6], temp_boxes[0])
		self.lessThan("0", "5", self.numbers[0], temp_boxes[0])
		self.play(FadeOut(self.left_pointer))
		self.shiftMergePointer()
		self.moveRemaining(self.numbers[5], temp_boxes[1])
		self.play(FadeOut(self.right_pointer))
		self.play(FadeOut(self.merge_pointer),
			FadeOut(self.boxes[5]), FadeOut(self.boxes[6])
		)

		self.boxes[5] = temp_boxes[0]
		self.boxes[6] = temp_boxes[1]

		self.play(
			AnimationGroup(
				FadeToColor(self.boxes[5], BLUE_C),
				FadeToColor(self.boxes[6], BLUE_C),
			)
		)

	def merge_8(self):
		temp_boxes = self.createTempBoxes(3, self.boxes[5], self.boxes[7])

		left_part = VGroup(
			self.boxes[5], self.boxes[6],
			self.numbers[0], self.numbers[5]
		)
		left_part.generate_target()
		left_part.target.shift(1.5 * DOWN)

		right_part = VGroup(
			self.boxes[7],
			self.numbers[2]
		)
		right_part.generate_target()
		right_part.target.shift(1.5 * DOWN)

		self.play(
			AnimationGroup(
				MoveToTarget(left_part),
				MoveToTarget(right_part),
				ShowCreation(temp_boxes[0]),
				ShowCreation(temp_boxes[1]),
				ShowCreation(temp_boxes[2]),
				lag_ratio=0.1
			)
		)

		self.showAllPointer(self.boxes[5], self.boxes[7], temp_boxes[0])
		self.lessThan("0", "2", self.numbers[0], temp_boxes[0])
		self.shiftLeftPointer()
		self.shiftMergePointer()
		self.greaterThan("5", "2", self.numbers[2], temp_boxes[1])
		self.play(FadeOut(self.right_pointer))
		self.shiftMergePointer()
		self.moveRemaining(self.numbers[5], temp_boxes[2])
		self.play(FadeOut(self.left_pointer))
		self.play(FadeOut(self.merge_pointer),
			FadeOut(self.boxes[5]), FadeOut(self.boxes[6]), FadeOut(self.boxes[7])
		)

		self.boxes[5] = temp_boxes[0]
		self.boxes[6] = temp_boxes[1]
		self.boxes[7] = temp_boxes[2]

		self.play(
			AnimationGroup(
				FadeToColor(self.boxes[5], BLUE_C),
				FadeToColor(self.boxes[6], BLUE_C),
				FadeToColor(self.boxes[7], BLUE_C)
			)
		)

	def split_10(self):
		self.showSplitPointer(self.boxes[8], self.boxes[9])

		left_part = VGroup(
			self.boxes[8],
			self.numbers[6]
		)

		right_part = VGroup(
			self.boxes[9], 
			self.numbers[8]
		)

		self.splitArray(left_part, right_part, 0.05)

	def merge_10(self):
		temp_boxes = self.createTempBoxes(2, self.boxes[8], self.boxes[9])

		left_part = VGroup(
			self.boxes[8],
			self.numbers[6]
		)
		left_part.generate_target()
		left_part.target.shift(1.5 * DOWN)

		right_part = VGroup(
			self.boxes[9], 
			self.numbers[8]
		)
		right_part.generate_target()
		right_part.target.shift(1.5 * DOWN)

		self.play(
			AnimationGroup(
				MoveToTarget(left_part),
				MoveToTarget(right_part),
				ShowCreation(temp_boxes[0]),
				ShowCreation(temp_boxes[1]),
				lag_ratio=0.1
			)
		)

		self.showAllPointer(self.boxes[8], self.boxes[9], temp_boxes[0])
		self.lessThan("6", "8", self.numbers[6], temp_boxes[0])
		self.play(FadeOut(self.left_pointer))
		self.shiftMergePointer()
		self.moveRemaining(self.numbers[8], temp_boxes[1])
		self.play(FadeOut(self.right_pointer))
		self.play(FadeOut(self.merge_pointer), FadeOut(self.boxes[8]), FadeOut(self.boxes[9]))

		self.boxes[8] = temp_boxes[0]
		self.boxes[9] = temp_boxes[1]

		self.play(
			AnimationGroup(
				FadeToColor(self.boxes[8], BLUE_C),
				FadeToColor(self.boxes[9], BLUE_C),
			)
		)

	def merge_7(self):
		temp_boxes = self.createTempBoxes(5, self.boxes[5], self.boxes[9])

		left_part = VGroup(
			self.boxes[5], self.boxes[6], self.boxes[7], 
			self.numbers[0], self.numbers[2], self.numbers[5]
		)
		left_part.generate_target()
		left_part.target.shift(1.5 * DOWN)

		right_part = VGroup(
			self.boxes[8], self.boxes[9],
			self.numbers[6], self.numbers[8]
		)
		right_part.generate_target()
		right_part.target.shift(1.5 * DOWN)

		self.play(
			AnimationGroup(
				MoveToTarget(left_part),
				MoveToTarget(right_part),
				ShowCreation(temp_boxes[0]),
				ShowCreation(temp_boxes[1]),
				ShowCreation(temp_boxes[2]),
				ShowCreation(temp_boxes[3]),
				ShowCreation(temp_boxes[4]),
				lag_ratio=0.1
			)
		)

		self.showAllPointer(self.boxes[5], self.boxes[8], temp_boxes[0])
		self.lessThan("0", "6", self.numbers[0], temp_boxes[0])
		self.shiftLeftPointer()
		self.shiftMergePointer()
		self.lessThan("2", "6", self.numbers[2], temp_boxes[1])
		self.shiftLeftPointer()
		self.shiftMergePointer()
		self.lessThan("5", "6", self.numbers[5], temp_boxes[2])
		self.play(FadeOut(self.left_pointer))
		self.shiftMergePointer()
		self.moveRemaining(self.numbers[6], temp_boxes[3])
		self.shiftRightPointer()
		self.shiftMergePointer()
		self.moveRemaining(self.numbers[8], temp_boxes[4])
		self.play(FadeOut(self.right_pointer))
		self.play(FadeOut(self.merge_pointer),
			FadeOut(self.boxes[5]), FadeOut(self.boxes[6]), FadeOut(self.boxes[7]), FadeOut(self.boxes[8]), FadeOut(self.boxes[9])
		)

		self.boxes[5] = temp_boxes[0]
		self.boxes[6] = temp_boxes[1]
		self.boxes[7] = temp_boxes[2]
		self.boxes[8] = temp_boxes[3]
		self.boxes[9] = temp_boxes[4]

		self.play(
			AnimationGroup(
				FadeToColor(self.boxes[5], BLUE_C),
				FadeToColor(self.boxes[6], BLUE_C),
				FadeToColor(self.boxes[7], BLUE_C),
				FadeToColor(self.boxes[8], BLUE_C),
				FadeToColor(self.boxes[9], BLUE_C),
			)
		)

	def merge_1(self):
		temp_boxes = self.createTempBoxes(10, self.boxes[0], self.boxes[9])

		left_part = VGroup(
			self.boxes[0], self.boxes[1], self.boxes[2], self.boxes[3], self.boxes[4],
			self.numbers[3], self.numbers[4], self.numbers[9], self.numbers[1], self.numbers[7]
		)
		left_part.generate_target()
		left_part.target.shift(1.5 * DOWN)

		right_part = VGroup(
			self.boxes[5], self.boxes[6], self.boxes[7], self.boxes[8], self.boxes[9],
			self.numbers[0], self.numbers[5], self.numbers[2], self.numbers[6], self.numbers[8]
		)
		right_part.generate_target()
		right_part.target.shift(1.5 * DOWN)

		self.play(
			AnimationGroup(
				MoveToTarget(left_part),
				MoveToTarget(right_part),
				ShowCreation(temp_boxes[0]),
				ShowCreation(temp_boxes[1]),
				ShowCreation(temp_boxes[2]),
				ShowCreation(temp_boxes[3]),
				ShowCreation(temp_boxes[4]),
				ShowCreation(temp_boxes[5]),
				ShowCreation(temp_boxes[6]),
				ShowCreation(temp_boxes[7]),
				ShowCreation(temp_boxes[8]),
				ShowCreation(temp_boxes[9]),
				lag_ratio=0.1
			)
		)

		self.showAllPointer(self.boxes[0], self.boxes[5], temp_boxes[0])
		self.greaterThan("1", "0", self.numbers[0], temp_boxes[0])
		self.shiftRightPointer()
		self.shiftMergePointer()
		self.lessThan("1", "2", self.numbers[1], temp_boxes[1])
		self.shiftLeftPointer()
		self.shiftMergePointer()
		self.greaterThan("3", "2", self.numbers[2], temp_boxes[2])
		self.shiftRightPointer()
		self.shiftMergePointer()
		self.lessThan("3", "5", self.numbers[3], temp_boxes[3])
		self.shiftLeftPointer()
		self.shiftMergePointer()
		self.lessThan("4", "5", self.numbers[4], temp_boxes[4])
		self.shiftLeftPointer()
		self.shiftMergePointer()
		self.greaterThan("7", "5", self.numbers[5], temp_boxes[5])
		self.shiftRightPointer()
		self.shiftMergePointer()
		self.greaterThan("7", "6", self.numbers[6], temp_boxes[6])
		self.shiftRightPointer()
		self.shiftMergePointer()
		self.lessThan("7", "8", self.numbers[7], temp_boxes[7])
		self.shiftLeftPointer()
		self.shiftMergePointer()
		self.greaterThan("9", "8", self.numbers[8], temp_boxes[8])
		self.play(FadeOut(self.right_pointer))
		self.shiftMergePointer()
		self.moveRemaining(self.numbers[9], temp_boxes[9])
		self.play(FadeOut(self.left_pointer))
		self.play(FadeOut(self.merge_pointer),
			FadeOut(self.boxes[0]), FadeOut(self.boxes[1]), FadeOut(self.boxes[2]), FadeOut(self.boxes[3]), FadeOut(self.boxes[4]),
			FadeOut(self.boxes[5]), FadeOut(self.boxes[6]), FadeOut(self.boxes[7]), FadeOut(self.boxes[8]), FadeOut(self.boxes[9])
		)

		self.boxes[0] = temp_boxes[0]
		self.boxes[1] = temp_boxes[1]
		self.boxes[2] = temp_boxes[2]
		self.boxes[3] = temp_boxes[3]
		self.boxes[4] = temp_boxes[4]
		self.boxes[5] = temp_boxes[5]
		self.boxes[6] = temp_boxes[6]
		self.boxes[7] = temp_boxes[7]
		self.boxes[8] = temp_boxes[8]
		self.boxes[9] = temp_boxes[9]

		self.play(
			AnimationGroup(
				FadeToColor(self.boxes[0], BLUE_C),
				FadeToColor(self.boxes[1], BLUE_C),
				FadeToColor(self.boxes[2], BLUE_C),
				FadeToColor(self.boxes[3], BLUE_C),
				FadeToColor(self.boxes[4], BLUE_C),
				FadeToColor(self.boxes[5], BLUE_C),
				FadeToColor(self.boxes[6], BLUE_C),
				FadeToColor(self.boxes[7], BLUE_C),
				FadeToColor(self.boxes[8], BLUE_C),
				FadeToColor(self.boxes[9], BLUE_C),
				lag_ratio=0.1
			)
		)

	def showSplitPointer(self, left_box, right_box):
		self.split_pointer.move_to(
			0.5 * (left_box.get_center() + right_box.get_center() + 1.5 * DOWN)
		)
		self.split_text.next_to(self.split_pointer, DOWN)
		self.play(
			DrawBorderThenFill(self.split_pointer),
			Write(self.split_text)
		)

	def splitArray(self, left, right, space):
		left.generate_target()
		left.target.shift(space * LEFT)

		right.generate_target()
		right.target.shift(space * RIGHT)

		self.play(
			MoveToTarget(left),
			MoveToTarget(right),
		)

		self.play(FadeOut(self.split_text), FadeOut(self.split_pointer))

	def createTempBoxes(self, n, left_most, right_most):
		temp_boxes = []

		for i in range(n):
			temp_boxes.append(
				Square(side_length=1.0, color=GRAY).move_to(0.5 * LEFT + i * RIGHT)
			)

		temp = VGroup(*temp_boxes).move_to(
			0.5 *(left_most.get_center() + right_most.get_center())
		)

		return temp_boxes

	def lessThan(self, left_val, right_val, num, target_box):
		highlight = VGroup(self.left_pointer, self.right_pointer)
		brace = Brace(highlight, DOWN)
		brace_text = TexMobject(left_val + " \\leq " + right_val).next_to(brace, DOWN)

		num.generate_target()
		num.target.move_to(target_box.get_center())

		self.play(GrowFromCenter(brace), Write(brace_text))
		self.play(MoveToTarget(num))
		self.play(FadeOut(brace), FadeOut(brace_text))

	def greaterThan(self, left_val, right_val, num, target_box):
		highlight = VGroup(self.left_pointer, self.right_pointer)
		brace = Brace(highlight, DOWN)
		brace_text = TexMobject(left_val + "\\text{ } \\textgreater \\text{ }" + right_val).next_to(brace, DOWN)

		num.generate_target()
		num.target.move_to(target_box.get_center())

		self.play(GrowFromCenter(brace), Write(brace_text))
		self.play(MoveToTarget(num))
		self.play(FadeOut(brace), FadeOut(brace_text))

	def showAllPointer(self, left, right, merge):
		self.left_pointer.next_to(left, DOWN)
		self.right_pointer.next_to(right, DOWN)
		self.merge_pointer.next_to(merge, UP)

		self.play(
			DrawBorderThenFill(self.left_pointer),
			DrawBorderThenFill(self.right_pointer),
			DrawBorderThenFill(self.merge_pointer)
		)

	def shiftMergePointer(self):
		self.merge_pointer.generate_target()
		self.merge_pointer.target.shift(RIGHT)
		self.play(MoveToTarget(self.merge_pointer))

	def shiftLeftPointer(self):
		self.left_pointer.generate_target()
		self.left_pointer.target.shift(RIGHT)
		self.play(MoveToTarget(self.left_pointer))

	def shiftRightPointer(self):
		self.right_pointer.generate_target()
		self.right_pointer.target.shift(RIGHT)
		self.play(MoveToTarget(self.right_pointer))

	def moveRemaining(self, num, box):
		num.generate_target()
		num.target.move_to(box.get_center())
		self.play(MoveToTarget(num))
