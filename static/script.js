document.addEventListener("DOMContentLoaded", () => {
    const div = document.querySelector(".auto-type");
    const texts = [
        "Study Online From The Comfort Of Your Home.",
        "With a Variety of Study Materials.",
        "Carry out Studying at Your Own Pace."
    ];
    let currentIndex = 0;

    function textTypingEffect(element, texts, i = 0, erase = false) {
        const text = texts[currentIndex];

        if (!erase) {
            element.textContent += text[i];

            if (i === text.length - 1) {
                setTimeout(() => textTypingEffect(element, texts, i, true), 1000); // Wait before erasing
            } else {
                setTimeout(() => textTypingEffect(element, texts, i + 1), 30);
            }
        } else {
            element.textContent = element.textContent.slice(0, -1);

            if (element.textContent.length === 0) {
                currentIndex = (currentIndex + 1) % texts.length; // Move to the next string
                setTimeout(() => textTypingEffect(element, texts), 1000); // Wait before typing again
            } else {
                setTimeout(() => textTypingEffect(element, texts, i, true), 30);
            }
        }
    }

    textTypingEffect(div, texts);
});
