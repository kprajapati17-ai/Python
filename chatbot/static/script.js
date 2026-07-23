// static/script.js
// Client script for the simplified, single-page offline chatbot interface.

document.addEventListener("DOMContentLoaded", () => {
    // DOM Elements
    const chatFeed = document.getElementById("chat-feed");
    const userInput = document.getElementById("user-input");
    const btnSend = document.getElementById("btn-send");
    const btnClear = document.getElementById("btn-clear");

    // Focus input on startup
    if (userInput) userInput.focus();

    // Key binding (Enter key to submit query)
    if (userInput) {
        userInput.addEventListener("keydown", (e) => {
            if (e.key === "Enter" && !userInput.disabled) {
                sendMessage();
            }
        });
    }

    if (btnSend) {
        btnSend.addEventListener("click", () => {
            if (!btnSend.disabled) sendMessage();
        });
    }
    
    if (btnClear) btnClear.addEventListener("click", clearChat);

    /**
     * Converts plain text with line breaks and markdown links into safe HTML.
     */
    function formatMessageText(text) {
        if (!text) return "";
        
        // 1. Escape HTML special characters to prevent XSS
        let escaped = text
            .replace(/&/g, "&amp;")
            .replace(/</g, "&lt;")
            .replace(/>/g, "&gt;")
            .replace(/"/g, "&quot;")
            .replace(/'/g, "&#039;");

        // 2. Convert markdown links [link text](url) to HTML <a> tags safely
        const linkRegex = /\[([^\]]+)\]\((https?:\/\/[^\s\)]+)\)/g;
        escaped = escaped.replace(linkRegex, (match, label, url) => {
            return `<a href="${url}" target="_blank" rel="noopener noreferrer" class="text-warning text-decoration-underline fw-semibold">${label}</a>`;
        });

        // 3. Convert line breaks \n to <br>
        return escaped.replace(/\n/g, "<br>");
    }

    function setInputState(disabled) {
        if (userInput) userInput.disabled = disabled;
        if (btnSend) btnSend.disabled = disabled;
    }

    function showTypingIndicator() {
        const indicator = document.createElement("div");
        indicator.id = "typing-indicator";
        indicator.className = "d-flex mb-4 bot-row";
        indicator.innerHTML = `
            <div class="bot-avatar me-2 d-flex align-items-center justify-content-center">
                <i class="bi bi-robot fs-6"></i>
            </div>
            <div class="rounded-3 p-3 bot-bubble text-white shadow-sm d-flex align-items-center gap-2" style="max-width: 80%;">
                <span class="small fw-semibold text-accent me-1">Assistant is typing</span>
                <span class="typing-dot"></span>
                <span class="typing-dot"></span>
                <span class="typing-dot"></span>
            </div>
        `;
        chatFeed.appendChild(indicator);
        chatFeed.scrollTop = chatFeed.scrollHeight;
    }

    function hideTypingIndicator() {
        const indicator = document.getElementById("typing-indicator");
        if (indicator) indicator.remove();
    }

    function sendMessage() {
        const query = userInput.value.trim();
        if (query === "") return;

        // 1. Append User bubble to feed (align right, green color)
        appendBubble("User", query, "user-row", "user-bubble", "bi-person-fill");
        
        // Clear input box and disable input controls while waiting
        userInput.value = "";
        setInputState(true);
        showTypingIndicator();

        // 2. Make Fetch POST request to Flask
        fetch("/ask", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message: query })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error("Server responded with status " + response.status);
            }
            return response.json();
        })
        .then(data => {
            hideTypingIndicator();
            // 3. Append Bot bubble to feed (align left, blue color)
            appendBubble("Bot", data.response, "bot-row", "bot-bubble", "bi-robot");
        })
        .catch(err => {
            console.error("AJAX Error:", err);
            hideTypingIndicator();
            appendBubble("Bot", "Error: Could not connect to the local Flask server.", "bot-row", "bot-bubble", "bi-robot");
        })
        .finally(() => {
            setInputState(false);
            if (userInput) userInput.focus();
        });
    }

    function appendBubble(sender, messageText, alignClass, bubbleClass, iconClass) {
        const row = document.createElement("div");
        row.className = `d-flex mb-4 ${alignClass}`;

        // Create avatar badge element
        const avatar = document.createElement("div");
        avatar.className = "bot-avatar d-flex align-items-center justify-content-center me-2";
        avatar.innerHTML = `<i class="bi ${iconClass} fs-6"></i>`;

        // Create text bubble card
        const bubble = document.createElement("div");
        bubble.className = `rounded-3 p-3 text-white shadow-sm ${bubbleClass}`;
        bubble.style.maxWidth = "80%";

        const header = document.createElement("div");
        header.className = "fw-bold text-accent mb-1";
        header.textContent = sender;

        const body = document.createElement("div");
        body.innerHTML = formatMessageText(messageText);

        bubble.appendChild(header);
        bubble.appendChild(body);
        
        // For alignment adjustments:
        if (alignClass === "user-row") {
            // user bubble is right aligned, we show bubble first, then avatar
            row.appendChild(bubble);
            // shift margins for user avatar
            avatar.classList.remove("me-2");
            avatar.classList.add("ms-2");
            row.appendChild(avatar);
        } else {
            // bot bubble is left aligned, we show avatar first, then bubble
            row.appendChild(avatar);
            row.appendChild(bubble);
        }
        
        chatFeed.appendChild(row);
        
        // Auto scroll to the bottom of the feed frame
        chatFeed.scrollTop = chatFeed.scrollHeight;
    }

    function clearChat() {
        chatFeed.innerHTML = `
            <div class="d-flex mb-4 bot-row">
                <div class="bot-avatar me-2 d-flex align-items-center justify-content-center">
                    <i class="bi bi-robot fs-6"></i>
                </div>
                <div class="rounded-3 p-3 bot-bubble text-white shadow-sm" style="max-width: 80%;">
                    <div class="fw-bold text-accent mb-1">Bot</div>
                    <div>Hello! Welcome to Easy Learn Academy. How can I help you today?</div>
                </div>
            </div>
        `;
        if (userInput) userInput.focus();
    }
});

