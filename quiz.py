def game():

    import pygame
    import sys

    # Initialize pygame
    pygame.init()

    # Set up screen dimensions
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Environmental Quiz Game")

    # Define colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    GRAY = (200, 200, 200)
    LIGHT_BLUE = (173, 216, 230)  # Background color
    DARK_BLUE = (0, 102, 204)
    YELLOW = (255, 255, 102)
    GRADIENT_START = (135, 206, 235)
    GRADIENT_END = (70, 130, 180)

    # Set up fonts
    font = pygame.font.Font(None, 40)
    small_font = pygame.font.Font(None, 30)

    # Define quiz questions
    quiz_data = [
        {
            "question": "How can we reduce air pollution?",
            "options": ["Plant more trees", "Burn more fuel", "Use plastic bags", "Increase car usage"],
            "answer": 0  # Index of the correct answer (A)
        },
        {
            "question": "What is the most environmentally friendly energy source?",
            "options": ["Coal", "Solar", "Gasoline", "Nuclear"],
            "answer": 1  # Index of the correct answer (B)
        },
        {
            "question": "How can we reduce water pollution?",
            "options": ["Dump waste in rivers", "Use fertilizers", "Reduce plastic waste", "Use chemicals"],
            "answer": 2  # Index of the correct answer (C)
        },
        {
            "question": "Which of the following can help fight climate change?",
            "options": ["Deforestation", "Fossil fuels", "Renewable energy", "Industrial waste"],
            "answer": 2  # Index of the correct answer (C)
        },
        {
            "question": "Which layer of the Earth's atmosphere contains the ozone layer?",
            "options": ["Troposphere", "Mesosphere", "Stratosphere", "Thermosphere"],
            "answer": 2  # Index of the correct answer (C)
        }
    ]

    # Variables for tracking the quiz state
    current_question = 0
    score = 0
    running = True
    selected_option = None
    submitted = False

    # Function to create a background gradient
    def draw_gradient():
        for i in range(HEIGHT):
            color = [
                GRADIENT_START[j] + (GRADIENT_END[j] - GRADIENT_START[j]) * i // HEIGHT
                for j in range(3)
            ]
            pygame.draw.line(screen, color, (0, i), (WIDTH, i))

    # Function to draw radio buttons
    def draw_radio_button(x, y, selected):
        outer_color = BLUE if selected else DARK_BLUE
        inner_color = YELLOW if selected else WHITE
        pygame.draw.circle(screen, outer_color, (x, y), 15, 2)  # Outer circle
        if selected:
            pygame.draw.circle(screen, inner_color, (x, y), 8)  # Inner filled circle

    # Function to render the quiz on the screen
    def render_quiz(question_data):
        draw_gradient()  # Draw the gradient background
        
        # Render the question
        question_text = font.render(question_data["question"], True, BLACK)
        question_rect = question_text.get_rect(center=(WIDTH // 2, 100))
        screen.blit(question_text, question_rect)

        # Render the options with radio buttons
        for i, option in enumerate(question_data["options"]):
            option_text = small_font.render(option, True, BLACK)
            option_rect = option_text.get_rect(midleft=(WIDTH // 2 - 40, 200 + i * 70))
            screen.blit(option_text, option_rect)
            draw_radio_button(WIDTH // 2 - 80, 215 + i * 70, selected_option == i)

        # Draw "Submit" button
        pygame.draw.rect(screen, DARK_BLUE, (WIDTH // 2 - 75, HEIGHT - 100, 150, 50))
        submit_text = font.render("Submit", True, WHITE)
        screen.blit(submit_text, (WIDTH // 2 - 50, HEIGHT - 90))

        pygame.display.flip()

    # Function to show feedback (green for correct, red for incorrect)
    def show_feedback(is_correct):
        color = GREEN if is_correct else RED
        message = "Correct!" if is_correct else "Wrong!"
        feedback_text = font.render(message, True, color)
        feedback_rect = feedback_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(feedback_text, feedback_rect)
        pygame.display.flip()
        pygame.time.delay(2000)  # Wait for 2 seconds

    # Main game loop
    while running:
        render_quiz(quiz_data[current_question])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                # Check if any radio button is clicked
                for i in range(4):
                    if WIDTH // 2 - 95 <= mouse_x <= WIDTH // 2 - 65 and 200 + i * 70 <= mouse_y <= 230 + i * 70:
                        selected_option = i
                # Check if submit button is clicked
                if WIDTH // 2 - 75 <= mouse_x <= WIDTH // 2 + 75 and HEIGHT - 100 <= mouse_y <= HEIGHT - 50:
                    if selected_option is not None and not submitted:
                        # Check if the selected option is correct
                        is_correct = selected_option == quiz_data[current_question]["answer"]
                        show_feedback(is_correct)
                        submitted = True
                        if is_correct:
                            score += 1  # Correct answer, earn a star
                            current_question += 1  # Move to the next question
                            selected_option = None  # Reset selected option
                            submitted = False  # Allow progression to the next question
                            if current_question >= len(quiz_data):
                                print(f"Congratulations! You earned {score} stars.")
                                running = False
                        else:
                            print(f"Game Over! You earned {score} stars.")
                            running = False

    # End of game
    pygame.quit()

game()