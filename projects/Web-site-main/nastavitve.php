<?php include 'header.php'; ?>

<main class="container my-5">
    <div class="page-card">
        <div class="page-header">
            <h1>Nastavitve</h1>
        </div>

        <div class="p-4 p-md-5">
            <p class="mb-4">Tukaj lahko spremenite barvo ozadja in uporabniško ime.</p>

            <form id="nastavitveForma">
                <div class="mb-4">
                    <label for="barva" class="form-label">Izberite barvo ozadja</label>
                    <input type="color" id="barva" name="barva" class="form-control form-control-color">
                </div>

                <div class="mb-4">
                    <label for="uporabnik" class="form-label">Vnesite svoje ime in priimek</label>
                    <input type="text" id="uporabnik" name="uporabnik" class="form-control" placeholder="Vnesi ime in priimek">
                </div>

                <button type="button" id="shraniBtn" class="btn btn-primary">Shrani</button>
                <div id="cookie-banner" class="cookie-banner hidden">
                    <p>Ta spletna stran uporablja piškotke za delovanje in izboljšanje uporabniške izkušnje.</p>
                    <button type="button" id="accept-cookies">Sprejmi</button>
                    <button type="button" id="decline-cookies">Zavrni</button>
                </div>
            </form>
        </div>
    </div>
</main>

<?php include 'footer.php'; ?>