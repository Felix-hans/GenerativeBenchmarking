type Robot struct {
    width  int
    height int
    x      int
    y      int
    dir    string
}

func Constructor(width int, height int) Robot {
    return Robot{
        width:  width,
        height: height,
        x:      0,
        y:      0,
        dir:    "East",
    }
}

func (r *Robot) Step(num int) {
    for i := 0; i < num; i++ {
        nx, ny := r.getNextPosition()
        if r.isOutOfBounds(nx, ny) {
            r.turnCounterclockwise()
            nx, ny = r.getNextPosition()
        }
        r.x = nx
        r.y = ny
    }
}

func (r *Robot) GetPos() []int {
    return []int{r.x, r.y}
}

func (r *Robot) GetDir() string {
    return r.dir
}

func (r *Robot) getNextPosition() (int, int) {
    switch r.dir {
    case "North":
        return r.x, r.y + 1
    case "East":
        return r.x + 1, r.y
    case "South":
        return r.x, r.y - 1
    case "West":
        return r.x - 1, r.y
    }
    return r.x, r.y
}

func (r *Robot) isOutOfBounds(x, y int) bool {
    return x < 0 || x >= r.width || y < 0 || y >= r.height
}

func (r *Robot) turnCounterclockwise() {
    switch r.dir {
    case "North":
        r.dir = "West"
    case "East":
        r.dir = "North"
    case "South":
        r.dir = "East"
    case "West":
        r.dir = "South"
    }
}