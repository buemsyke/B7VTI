/**
 * Circuit Loader - Hilfsfunktionen zum Laden von Falstad-CircuitJS1-Schaltungen
 * via iframe in eine HTML-Seite.
 *
 * Verwendung in einer Versuchsseite:
 *
 *   <iframe id="simulator" sandbox="allow-scripts allow-same-origin allow-popups"></iframe>
 *   <script src="../../../assets/js/circuit-loader.js"></script>
 *   <script>
 *     const circuit = `$ 1 0.000005 ...
 * v 192 368 192 144 0 0 40 5 0 0 0.5
 * ...`;
 *     CircuitLoader.loadCircuit('simulator', circuit, '../../../assets/falstad');
 *   </script>
 */
const CircuitLoader = {
    defaultParams: {
        euroResistors: 'true',
        whiteBackground: 'true',
        conventionalCurrent: 'true',
        running: 'true',
        editable: 'true',
        hideMenu: 'false',
        hideSidebar: 'false',
        zoom: '200'
    },

    buildFalstadUrl(circuitText, basePath = '../../../assets/falstad', extraParams = {}) {
        const params = { ...this.defaultParams, ...extraParams };
        const encoded = encodeURIComponent(circuitText.trim());

        let url = `${basePath}/circuitjs.html?cct=${encoded}`;
        for (const [key, value] of Object.entries(params)) {
            url += `&${key}=${encodeURIComponent(value)}`;
        }
        return url;
    },

    loadCircuit(iframeId, circuitText, basePath = '../../../assets/falstad', extraParams = {}) {
        const iframe = document.getElementById(iframeId);
        if (!iframe) {
            console.error(`iframe mit ID "${iframeId}" nicht gefunden.`);
            return;
        }
        iframe.src = this.buildFalstadUrl(circuitText, basePath, extraParams);
        iframe.addEventListener('load', () => {
            const loading = iframe.parentElement?.querySelector('.simulator-loading');
            if (loading) loading.style.display = 'none';
        });
    },

    toggleInfo() {
        const info = document.querySelector('.exercise-info');
        const btn = document.querySelector('.toggle-info-btn');
        if (info && btn) {
            info.classList.toggle('collapsed');
            btn.classList.toggle('collapsed');
            const isCollapsed = info.classList.contains('collapsed');
            btn.innerHTML = isCollapsed
                ? '<span class="arrow">▲</span> Aufgabenstellung einblenden'
                : '<span class="arrow">▼</span> Aufgabenstellung ausblenden';
        }
    }
};

document.addEventListener('DOMContentLoaded', () => {
    const toggleBtn = document.querySelector('.toggle-info-btn');
    if (toggleBtn) {
        toggleBtn.addEventListener('click', () => CircuitLoader.toggleInfo());
    }
    document.querySelectorAll('.solution-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            const wrapper = btn.closest('.solution-toggle');
            if (wrapper) {
                const isShown = wrapper.classList.toggle('show');
                btn.textContent = isShown
                    ? 'Beispiellösung ausblenden'
                    : 'Beispiellösung anzeigen';
            }
        });
    });
});
