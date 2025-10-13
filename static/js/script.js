document.addEventListener("DOMContentLoaded", () => {
    const chatForm = document.getElementById("chat-form");
    const chatBox = document.getElementById("chat-box");
    const userInput = document.getElementById("user-input");

    // Function to create and append messages to the chat box
    const appendMessage = (message, sender, isLoading = false) => {
        const messageDiv = document.createElement("div");
        messageDiv.classList.add("message", sender);
        if (isLoading) {
            messageDiv.classList.add("loading");
        }
        messageDiv.textContent = message;
        chatBox.appendChild(messageDiv);
        chatBox.scrollTop = chatBox.scrollHeight; // Auto-scroll to the latest message
    };

    // Function to remove the loading indicator
    const removeLoadingIndicator = () => {
        const loadingMessage = document.querySelector(".message.loading");
        if (loadingMessage) loadingMessage.remove();
    };

    // Function to handle AI responses
    const handleAIResponse = async (userMessage) => {
        try {
            const response = await fetch("/api/chat", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ message: userMessage }),
            });

            const data = await response.json();
            removeLoadingIndicator();

            if (data.response) {
                appendMessage(`Amro Response: ${data.response}`, "ai");
            } else if (data.error) {
                appendMessage(`Amro Response: ${data.error}`, "ai");
            } else {
                appendMessage("Amro Response: Unexpected error occurred.", "ai");
            }
        } catch (error) {
            console.error("Error:", error);
            removeLoadingIndicator();
            appendMessage("Amro Response: Oops! Something went wrong. Please try again.", "ai");
        }
    };

    // Handle form submission
    chatForm.addEventListener("submit", (event) => {
        event.preventDefault();
        const userMessage = userInput.value.trim();

        if (!userMessage) return;

        // Display the user's message
        appendMessage(`You: ${userMessage}`, "user");
        userInput.value = "";

        // Display loading indicator
        appendMessage("Amro AI is thinking...", "ai", true);

        // Process the AI response
        handleAIResponse(userMessage);
    });
});
