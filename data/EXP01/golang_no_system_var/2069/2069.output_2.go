type Robot struct {
    width, height int
    x, y          int
    direction     string
}

func Constructor(width int, height int) Robot {
    return Robot{
        width:     width,
        height:    height,
        x:         0,
        y:         0,
        direction: "East",
    }
}

func (r *Robot) Step(num int) {
    for i := 0; i < num; i++ {
        newX, newY := r.getNextPosition()
        if r.isOutOfBounds(newX, newY) {
            r.rotate90Degrees()
            continue
        }
        r.x = newX
        r.y = newY
    }
}

func (r *Robot) GetPos() []int {
    return []int{r.x, r.y}
}

func (r *Robot) GetDir() string {
    return r.direction
}

func (r *Robot) getNextPosition() (int, int) {
    newX, newY := r.x, r.y
    if r.direction == "North" {
        newY++
    } else if r.direction == "East" {
        newX++
    } else if r.direction == "South" {
        newY--
    } else if r.direction == "West" {
        newX--
    }
    return newX, newY
}

func (r *Robot) isOutOfBounds(x, y int) bool {
    return x < 0 || y < 0 || x >= r.width || y >= r.height
}

func (r *Robot) rotate90Degrees() {
    if r.direction == "North" {
        r.direction = "West"
    } else if r.direction == "West" {
        r.direction = "South"
    } else if r.direction == "South" {
        r.direction = "East"
    } else if r.direction == "East" {
        r.direction = "North"
    }
}