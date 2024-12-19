-- Size of the board
local boardSize = 8
local squareSize = 60

-- 2D array to store the board values
local board = {}

-- Initialize the board (empty squares for now)
function love.load()
    -- Initialize the chessboard array with nil (empty)
    for row = 1, boardSize do
        board[row] = {}
        for col = 1, boardSize do
            -- You can initialize with pieces or leave them as nil (empty)
            board[row][col] = nil  -- Empty square
        end
    end
end

function love.draw()
    -- Draw the chessboard with (1,1) at the bottom-left
    for row = 1, boardSize do
        for col = 1, boardSize do
            -- Alternate the square colors: white for even and black for odd
            if (row + col) % 2 == 1 then
                love.graphics.setColor(1, 1, 1)  -- White square
            else
                love.graphics.setColor(0, 0, 0)  -- Black square
            end

            -- Draw the square: start from the bottom-left (1,1) as the corner
            love.graphics.rectangle("fill", (col - 1) * squareSize, (boardSize - row) * squareSize, squareSize, squareSize)

     
        end
    end
end
