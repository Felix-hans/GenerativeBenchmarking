type Robot struct {
	width, height   int
	x, y            int
	direction       string
}

func NewRobot(width int, height int) *Robot {
	return &Robot{
		width:     width,
		height:    height,
		x:         0,
		y:         0,
		direction: "East",
	}
}

func (r *Robot) Step(num int) {
	for num > 0 {
		switch r.direction {
		case "North":
			r.y++
			if r.y >= r.height {
				r.y--
				r.direction = "West"
			}
		case "East":
			r.x++
			if r.x >= r.width {
				r.x--
				r.direction = "North"
			}
		case "South":
			r.y--
			if r.y < 0 {
				r.y++
				r.direction = "East"
			}
		case "West":
			r.x--
			if r.x < 0 {
				r.x++
				r.direction = "South"
			}
		}
		num--
	}
}

func (r *Robot) GetPos() []int {
	return []int{r.x, r.y}
}

func (r *Robot) GetDir() string {
	return r.direction
}


