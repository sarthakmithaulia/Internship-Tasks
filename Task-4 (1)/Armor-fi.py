from bs4 import BeautifulSoup
import re
import json
headers = {
  'Cookie': 'ASP.NET_SessionId=sv5fsfd33v4oiwjoqcb0r2ib',
  'authority': 'etherscan.io',
  'accept-language': 'en-US,en;q=0.8',
  'cookie': 'etherscan_offset_datetime=+5.5; __stripe_mid=1ede3194-2257-418c-9ffd-01d2193512df9465f3; displaymode=dim; etherscan_pwd=4792:Qdxb:wmycqobgs7pW0Bv6cYEyWU4fVj6t7QP+NS/OOHbAOiI=; etherscan_userid=sarthakM; etherscan_autologin=True; ASP.NET_SessionId=n10u0k3qlugy5yedgg4d1uvl; __cflb=02DiuFnsSsHWYH8WqVXcJWaecAw5gpnmdqya6rNC7fqwS; cf_chl_3=d757441bc1a9ddf; cf_clearance=4P5nUw45u33s_XO3q8Zdrk3psxWWrX8nSK9eH6nql6s-1705485242-1-ATRQ8vXpJ1AS9q7BdQXDK0XRwhzrt6mBPlKTP2WehLmkEbwd97G2JsvBQDHSeQ2obdy9sYEXA7F2K0/B2npJhuE=',
  'referer': 'https://etherscan.io/labelcloud',
  'sec-ch-ua': 'Not_A',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': 'Windows',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-user': '?1',
  'sec-gpc': '1',
  'upgrade-insecure-requests': '1'
}

html_content='''


<!doctype html>
<html id="html" lang="en">
<head><title>
	Ethereum Top Accounts by ETH Balance | Etherscan
</title><meta charset="utf-8" /><meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" /><meta name="author" content="etherscan.io" /><meta name="Description" content="The top accounts in Ethereum in descending order by the number of Ether (ETH) balance in an account and the percentage of the Ether (ETH) that the account hold." /><meta name="keywords" content="ethereum, explorer, ether, search, blockchain, crypto, currency" /><meta name="format-detection" content="telephone=no" />
<meta property="og:title" content="Ethereum Top Accounts by ETH Balance | Etherscan" /> <meta property="og:description" content="The top accounts in Ethereum in descending order by the number of Ether (ETH) balance in an account and the percentage of the Ether (ETH) that the account hold." /> <meta property="og:type" content="website" /> <meta property="og:site_name" content="Ethereum (ETH) Blockchain Explorer" /> <meta property="og:url" content="http://etherscan.io/accounts" /> <meta property="og:image" content="https://etherscan.io/images/brandassets/etherscan-logo-circle.jpg" /> <meta property="og:image:url" content="https://etherscan.io/images/brandassets/etherscan-logo-r.jpg" /> <meta property="og:image:alt" content="Visit Etherscan.io" /> <meta name="twitter:card" content="summary" /> <meta name="twitter:title" content="Ethereum Top Accounts by ETH Balance | Etherscan" /> <meta property="twitter:description" content="The top accounts in Ethereum in descending order by the number of Ether (ETH) balance in an account and the percentage of the Ether (ETH) that the account hold." /> <meta name="twitter:site" content="@etherscan" /> <meta property="twitter:image" content="https://etherscan.io/images/brandassets/etherscan-logo-circle.jpg" />
<link rel="shortcut icon" href="/images/favicon3.ico" />
<script async src="https://www.googletagmanager.com/gtag/js?id=G-T1JC9RNQXV"></script>
<script>
        window.dataLayer = window.dataLayer || [];
        function gtag() { dataLayer.push(arguments); }
        gtag('js', new Date());
        gtag('config','G-T1JC9RNQXV', { 'anonymize_ip': true });
    </script>
<script>
        //Search box text ad
        var availableAd = [];
        var gotAd = [];

        
        availableAd = ["<div class='p-2'><a href='https://moonpay-affiliate-program.sjv.io/GmG56B' rel='nofollow' target='_blank' data-bs-toggle='tooltip' data-bs-trigger='hover' title='Links to an External Advertiser site' class='search-panel-ads d-flex align-items-center p-2 rounded'><div class='me-2'><img width='22' class='rounded-1' src='/images/gen/moonpay_20.png' alt='Ads'></div><div class='text-truncate'><h6 class='d-flex align-items-center fs-sm text-dark mb-0'><div class='text-truncate me-2'>Moonpay: Buy & Sell Crypto with a credit card.</div><span class='d-none d-sm-inline-block small bg-white text-muted rounded-1 border px-2 py-1 ms-1'>Sponsored</span><span class='d-inline-block d-sm-none small bg-white text-muted rounded-1 border px-2 py-1 ms-1'>Ad</span></h6></div></a></div>", "<div class='p-2'><a href='https://goto.etherscan.com/rd/ZF7T982PESC5ATRI95AW6JIEW' rel='nofollow' target='_blank' data-bs-toggle='tooltip' data-bs-trigger='hover' title='Links to an External Advertiser site' class='search-panel-ads d-flex align-items-center p-2 rounded'><div class='me-2'><img width='22' class='rounded-1' src='/images/gen/cons_20.png' alt='Ads'></div><div class='text-truncate'><h6 class='d-flex align-items-center fs-sm text-dark mb-0'><div class='text-truncate me-2'>Get Started with MetaMask Portfolio</div><span class='d-none d-sm-inline-block small bg-white text-muted rounded-1 border px-2 py-1 ms-1'>Sponsored</span><span class='d-inline-block d-sm-none small bg-white text-muted rounded-1 border px-2 py-1 ms-1'>Ad</span></h6></div></a></div>"];
        gotAd = ["ShowAds					"];
        
    </script>

<link rel="preconnect" href="https://fonts.googleapis.com" /><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin /><link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&amp;display=swap" rel="stylesheet" />
<link rel="stylesheet" href="/assets/vendor/font-awesome/css/all.min.css?v=24.2.1.2">
<link rel="stylesheet" href="/assets/vendor/autocomplete/dist/css/autocomplete.min.css?v=24.2.1.2" />
<link rel="stylesheet" href="/assets/css/theme.min.css?v=24.2.1.2">
<link rel="stylesheet" href="/assets/css/custom.css?v=24.2.1.2">
<script src="/assets/vendor/jquery/dist/jquery.min.js?v=24.2.1.2"></script>
<script type="text/javascript" src="/jss/blockies.js?v=24.2.1.2"></script>
<script type="text/javascript" src="/assets/js/theme-appearance.js?v=24.2.1.2"></script>
<style>
        .autolink-safari a {
            pointer-events: none !important;
            text-decoration: none !important;
            color: inherit !important;
        }
    </style>
<style> .dyvtpvbr3su { -ms-flex-pack: center; justify-content: center; } .a7bznr4p3ah { border-top: 1px solid #e7eaf3 !important; } body.dark-mode .a7bznr4p3ah { border-color: #18365b !important; } @media (min-width: 992px) { .b48c4wuxzpq { display: block !important; } } @media (min-width: 992px) { .ckzp8wx6gcg { display: inline-block !important; } }  </style>
<link rel="stylesheet" type="text/css" href="/assets/vendor/datatables/datatables.min.css?v=24.2.1.2" />
<style>
        .card-header.sticky-card-header {
            position: sticky;
            top: 0;
            z-index: 10;
        }

        .dataTable > thead > tr > th[class*="remove-icon"]:before,
        .dataTable > thead > tr > th[class*="remove-icon"]:after {
            content: "" !important;
        }

        table.dataTable thead th.sorting:before,
        table.dataTable thead th.sorting_asc:before,
        table.dataTable thead th.sorting_desc:before,
        table.dataTable thead th.sorting:after,
        table.dataTable thead th.sorting_asc:after,
        table.dataTable thead th.sorting_desc:after {
            content: none;
        }

        .dataTables_processing {
            z-index: 100;
        }

        .hideFooter {
            display: none;
        }

        table tfoot th {
            font-weight: 400;
        }

        .fadeout {
            position: relative;
            bottom: 4em;
            height: 4em;
            background: -webkit-linear-gradient( rgba(255, 255, 255, 0) 0%, rgba(255, 255, 255, 1) 100% );
            background-image: -moz-linear-gradient( rgba(255, 255, 255, 0) 0%, rgba(255, 255, 255, 1) 100% );
            background-image: -o-linear-gradient( rgba(255, 255, 255, 0) 0%, rgba(255, 255, 255, 1) 100% );
            background-image: linear-gradient( rgba(255, 255, 255, 0) 0%, rgba(255, 255, 255, 1) 100% );
            background-image: -ms-linear-gradient( rgba(255, 255, 255, 0) 0%, rgba(255, 255, 255, 1) 100% )
        }

        table.dataTable {
	        margin-bottom: 0 !important;
        }
    </style>
<script type="text/javascript" src="/assets/vendor/datatables/datatables.min.js?v=24.2.1.2"></script>
<script>

        function showSignInPopUp(tableid) {
            if ($('#signInPopUp_' + tableid).attr("style")) {
                $('#signInPopUp_' + tableid).removeAttr("style");
                $('#signInPopUp_' + tableid).addClass("show").addClass("active");
            }

            if (!$('#paywall_mask_' + tableid).hasClass("paywall-mask")) {
                $('#paywall_mask_' + tableid).addClass("paywall-mask");
            }

            return;
        }

        function hideSignInPopUp(tableid) {
            if (!$('#signInPopUp_' + tableid).attr("style")) {
                $('#signInPopUp_' + tableid).attr("style", "display:none;");
                $('#signInPopUp_' + tableid).removeClass("show").removeClass("active");
            }

            if ($('#paywall_mask_' + tableid).hasClass("paywall-mask")) {
                $('#paywall_mask_' + tableid).removeClass("paywall-mask");
            }

            return;
        }
    </script>
</head>
<body id="body" class="d-flex flex-column min-vh-100">
<section id="masterNoticeBar">


</section>

<section id="masterTopBar" class="sticky-top bg-white border-bottom py-2 d-print-none">
<div class="container-xxl d-flex align-items-center justify-content-between">
<div id="ethPrice" class="d-none d-md-flex align-items-center gap-4 w-100 fs-sm">
<div class="text-muted"><span class="text-muted">ETH Price:</span> <a href="/chart/etherprice">$2,303.81</a><span data-bs-toggle="tooltip" data-bs-placement="top" title="Changes in the last 24 hours"><span class="text-danger"> (-0.43%)</span></span></div><div class="text-muted d-none d-lg-block"><i class="fad fa-gas-pump me-1"></i> Gas: <span id="spanGasTooltip" data-bs-toggle="tooltip" data-bs-html="true" title="Base Fee: 15 Gwei<br>Priority Fee: 0 Gwei"><a href="/gastracker"><span class="gasPricePlaceHolder">15</span> Gwei</a></span></div>
</div>
<div class="d-flex justify-content-end align-items-center gap-2 w-100">
<div id="frmMaster" class="search-panel-container flex-grow-1 position-relative" style="width: 30rem;">
<form action="/search" method="GET" autocomplete="off" spellcheck="false" class="auto-search-max-height">
<span class="d-flex align-items-center position-absolute top-0 bottom-0" title="Search" style="left: 0.75rem;">
<i class="fa-regular fa-search fs-5 text-secondary"></i>
</span>
<input type="text" class="form-control form-control-lg bg-light bg-focus-white pe-20" autocomplete="off" spellcheck="false" id="search-panel" name="q" placeholder="Search by Address / Txn Hash / Block / Token / Domain Name" aria-describedby="button-header-search" onkeyup="handleSearchText(this);" maxlength="68" style="padding-left: 2.375rem;" />
<a href="javascript:;" class="clear-icon d-none align-items-center position-absolute top-0 bottom-0 my-auto d-flex align-items-center" style="right: 3.375rem; cursor:pointer;">
<i class="fa-regular fa-xmark fs-5 text-secondary"></i>
</a>
<a href="javascript:;" class="search-icon d-none btn btn-sm btn-white my-1.5 align-items-center position-absolute top-0 bottom-0 d-flex align-items-center" style="right: 0.75rem; cursor:pointer;">
<i class="fa-regular fa-arrow-turn-down-left text-secondary"></i>
</a>
<input type="hidden" value id="hdnSearchText" />
<input type="hidden" value id="hdnSearchLabel" />
<input id="hdnIsTestNet" value="False" type="hidden" />
<span class="shortcut-slash-icon align-items-center position-absolute top-0 bottom-0 align-items-center d-none d-sm-flex" title="Search" style="right: 0.5rem;">
<kbd class="bg-dark bg-opacity-25 fw-semibold px-2 py-0.5 text-white">/</kbd>
</span>
</form>
</div>
<div id="divThemeSetting" class="dropdown d-none d-lg-block">
<button class="btn btn-lg btn-white text-primary content-center" type="button" id="dropdownMenuTopbarSettings" data-bs-auto-close="outside" data-bs-toggle="dropdown" aria-expanded="false" style="width: 2.375rem; height: 2.375rem;">
<span class="theme-btn-main"><i class="far fa-sun-bright theme-icon-active" data-href="#fa-sun-bright"></i></span>
</button>
<ul class="dropdown-menu dropdown-menu-end" aria-labelledby="dropdownMenuTopbarSettings">
<li>
<button type="button" class="dropdown-item theme-btn active" data-bs-theme-value="light" onclick="setThemeMode('light');">
<i class="far fa-sun-bright fa-fw dropdown-item-icon theme-icon me-1" data-href="#fa-sun-bright"></i> Light
</button>
</li>
<li>
<button type="button" class="dropdown-item theme-btn" data-bs-theme-value="dim" onclick="setThemeMode('dim');">
<i class="far fa-moon-stars fa-fw dropdown-item-icon theme-icon me-1" data-href="#fa-moon-stars"></i> Dim
</button>
</li>
<li>
<button type="button" class="dropdown-item theme-btn" data-bs-theme-value="dark" onclick="setThemeMode('dark');">
<i class="far fa-moon fa-fw dropdown-item-icon theme-icon me-1" data-href="#fa-moon"></i> Dark
</button>
</li>
<li>
<hr class="dropdown-divider">
</li>
<li>
<a class="dropdown-item" href="/settings">
<i class="far fa-gear fa-fw dropdown-item-icon me-1"></i> Site Settings <i class="far fa-arrow-right ms-1"></i>
</a>
</li>
</ul>
</div>
<div id="divTestNet" class="dropdown d-none d-lg-block">
<button class="btn btn-lg btn-white content-center" type="button" id="dropdownTopbarNetworks" data-bs-toggle="dropdown" aria-expanded="false" style="width: 2.375rem; height: 2.375rem;">
<img width="10" data-img-theme="light" src="/images/svg/brands/ethereum-original.svg" alt="Ethereum Logo">
<img width="10" data-img-theme="darkmode" src="/images/svg/brands/ethereum-original-light.svg" alt="Ethereum Logo">
</button>
<ul class="dropdown-menu dropdown-menu-end" aria-labelledby="dropdownTopbarNetworks">
<li>
<a href="https://etherscan.io" id="LI_Mainnet" class="dropdown-item active active">
Ethereum Mainnet
</a>
</li>
<li>
<a href="https://cn.etherscan.com/?lang=zh-CN" id="LI_Mainnet_CN" class="dropdown-item">
Ethereum Mainnet <span class="badge border bg-light text-dark ms-1">CN</span>
</a>
</li>
<li>
<a href="https://beaconscan.com/" id="LI2" class="dropdown-item">
Beaconscan <span class="badge border bg-light text-dark ms-1">ETH2</span>
</a>
</li>
<li>
<hr class="dropdown-divider">
</li>
<li>
<a href="https://goerli.etherscan.io" id="LI58" class="dropdown-item">
Goerli Testnet
</a>
</li>
<li>
<a href="https://sepolia.etherscan.io" id="LI9" class="dropdown-item">
Sepolia Testnet
</a>
</li>
<li>
<a href="https://holesky.etherscan.io" id="A2" class="dropdown-item">
Holesky Testnet
</a>
</li>
</ul>
</div>
</div>
</div>
</section>


<header id="masterHeader" class="header border-bottom d-print-none">
<nav class="navbar navbar-expand-lg navbar-light py-3 py-lg-0">
<div class="container-xxl position-relative">
<a class="navbar-brand" href="/" target="_parent" aria-label="Etherscan">
<img width="150" data-img-theme="light" src="/assets/svg/logos/logo-etherscan.svg?v=0.0.5" alt="Etherscan Logo">
<img width="150" data-img-theme="darkmode" src="/assets/svg/logos/logo-etherscan-light.svg?v=0.0.5" alt="Etherscan Logo">
</a>
<div class="d-flex align-items-center gap-4">
<button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
<span class="navbar-toggler-icon"></span>
</button>
</div>
<div class="collapse navbar-collapse justify-content-end" id="navbarSupportedContent">
<ul class="navbar-nav gap-1 gap-lg-0 pt-4 pt-lg-0">
<li class="nav-item">
<a href="/" id="LI_default" class="nav-link" aria-current="page">
Home
</a>
</li>

<li class="nav-item dropdown">
<a href="javascript:;" id="LI_blockchain" class="nav-link dropdown-toggle active" role="button" data-bs-toggle="dropdown" aria-expanded="false">Blockchain</a>
<ul class="dropdown-menu dropdown-menu-border" style="min-width: 14rem;">
<li>
<a href="/txs" id="LI12" class="dropdown-item">
Transactions
</a>
</li>
<li>
<a href="/txsPending" id="LI16" class="dropdown-item">
Pending Transactions
</a>
</li>
<li>
<a href="/txsInternal" id="LI14" class="dropdown-item">
Contract Internal Transactions
</a>
</li>
<li>
<a href="/txsBeaconDeposit" id="LI22" class="dropdown-item">
Beacon Deposits
</a>
</li>
<li>
<a href="/txsBeaconWithdrawal" id="LI_BeaconWithdrawals" class="dropdown-item">
Beacon Withdrawals
</a>
</li>
<li>
<hr class="dropdown-divider">
</li>
<li>
<a href="/blocks" id="LI_blocks" class="dropdown-item">
View Blocks
</a>
</li>
<li>
<a href="/blocks_forked" id="LI_blocks2" class="dropdown-item">
Forked Blocks (Reorgs)
</a>
</li>
<li>
<a href="/uncles" id="LI8" class="dropdown-item">
Uncles
</a>
</li>
<li>
<hr class="dropdown-divider">
</li>
<li>
<a href="/accounts" id="LI_accountall" class="dropdown-item">
Top Accounts
</a>
</li>
<li>
<a href="/contractsVerified" id="LI_contract_verified" class="dropdown-item">
Verified Contracts
</a>
</li>
</ul>
</li>


<li class="nav-item dropdown">
<a href="javascript:;" id="LI_tokens" class="nav-link dropdown-toggle" role="button" data-bs-toggle="dropdown" aria-expanded="false">Tokens</a>
<ul class="dropdown-menu dropdown-menu-border" style="min-width: 14rem;">
<li>
<a href="/tokens" id="LI21" class="dropdown-item">
Top Tokens <span class="small text-muted">(ERC-20)</span>
</a>
</li>
<li>
<a href="/tokentxns" id="LI1" class="dropdown-item">
Token Transfers <span class="small text-muted">(ERC-20)</span>
</a>
</li>
</ul>
</li>


<li class="nav-item dropdown">
<a href="javascript:;" id="LI_Nfts" class="nav-link dropdown-toggle" role="button" data-bs-toggle="dropdown" aria-expanded="false">NFTs</a>
<ul class="dropdown-menu dropdown-menu-border" style="min-width: 14rem;">
<li>
<a href="/nft-top-contracts" id="LI63" class="dropdown-item">
Top NFTs
</a>
</li>
<li>
<a href="/nft-top-mints" id="LI67" class="dropdown-item">
Top Mints
</a>
</li>
<li>
<a href="/nft-trades" id="LI64" class="dropdown-item">
Latest Trades
</a>
</li>
<li>
<a href="/nft-transfers" id="LI65" class="dropdown-item">
Latest Transfers
</a>
</li>
<li>
<a href="/nft-latest-mints" id="LI66" class="dropdown-item">
Latest Mints
</a>
</li>
</ul>
</li>




<li class="nav-item dropdown">
<a href="javascript:;" id="LI_resources" class="nav-link dropdown-toggle" role="button" data-bs-toggle="dropdown" aria-expanded="false">Resources</a>
<ul class="dropdown-menu dropdown-menu-border" style="min-width: 14rem;">
<li>
<a href="/charts" id="LI_charts2" class="dropdown-item">
Charts And Stats
</a>
</li>
<li>
<a href="/topstat" id="LI_topstat" class="dropdown-item">
Top Statistics
</a>
</li>
<li>
<a href="/leaderboard" id="LI_Leaderboard" class="dropdown-item">
Leaderboard
</a>
</li>
<li>
<hr class="dropdown-divider">
</li>
<li>
<a href="/directory" id="LI62" class="dropdown-item">
Directory
</a>
</li>
<li>
<a href="https://info.etherscan.com/newsletters/" id="LI60" class="dropdown-item">
Newsletter
</a>
</li>
<li>
<a href="https://info.etherscan.com/" id="LI61" class="dropdown-item">
Knowledge Base
</a>
</li>
</ul>
</li>


<li class="nav-item dropdown">
<a href="../../#" id="li_developers" class="nav-link dropdown-toggle" role="button" data-bs-toggle="dropdown" aria-expanded="false">Developers</a>
<ul class="dropdown-menu dropdown-menu-border" style="min-width: 14rem;">
<li>
<a href="/apis" id="LI5" class="dropdown-item">
API Plans
</a>
</li>
<li>
<a href="https://docs.etherscan.io/" id="LI6" class="dropdown-item" target="_blank">
API Documentation
</a>
</li>
<li>
<hr class="dropdown-divider">
</li>
<li>
<a href="/code-reader" id="A1" class="dropdown-item">
Code Reader <span class="badge border bg-light text-muted">Beta</span>
</a>
</li>
<li>
<a href="/verifyContract" id="LI17" class="dropdown-item">
Verify Contract
</a>
</li>
<li>
<a href="/find-similar-contracts" id="LI55" class="dropdown-item">
Similar Contract Search
</a>
</li>
<li>
<a href="/searchcontract" id="LI53" class="dropdown-item">
Smart Contract Search
</a>
</li>
<li>
<a href="/contractdiffchecker" id="LI54" class="dropdown-item">
Contract Diff Checker
</a>
</li>
<li>
<hr class="dropdown-divider">
</li>
<li>
<a href="/vyper" id="LI27" class="dropdown-item">
Vyper Online Compiler
</a>
</li>
<li>
<a href="/opcode-tool" id="LI24" class="dropdown-item">
Bytecode to Opcode
</a>
</li>
<li>
<a href="/pushTx" id="LI10" class="dropdown-item">
Broadcast Transaction
</a>
</li>
</ul>
</li>


<li class="nav-item dropdown position-initial">
<a href="javascript:;" id="LI_services2" class="nav-link dropdown-toggle" role="button" data-bs-toggle="dropdown" aria-expanded="false">More</a>
<div class="dropdown-menu dropdown-menu-border dropdown-menu-mega">
<div class="row">
<div class="col-lg order-last order-lg-first">
<div class="d-flex flex-column bg-light h-100 rounded-3 p-5">
<div>
<h6>Tools &amp; Services</h6>
<p>Discover more of Etherscan's tools and services in one place.</p>
</div>
<div class="mt-auto">
<p class="text-muted mb-2">Sponsored</p>
<a target="_blank" href="https://chat.blockscan.com">
<img width="140" data-img-theme="light" src="/images/svg/blockscan-logo-light.svg?v=0.0.5" alt />
<img width="140" data-img-theme="dim" src="/images/svg/blockscan-logo-dark.svg?v=0.0.5" alt />
<img width="140" data-img-theme="dark" src="/images/svg/blockscan-logo-dark.svg?v=0.0.5" alt />
</a>
</div>
</div>
</div>
<div class="col-sm py-5">
<h6 class="px-3 mb-3">Tools</h6>
<ul class="list-unstyled">
<li>
<a href="/unitconverter" id="LI50" class="dropdown-item">
<i class="far fa-arrows-rotate dropdown-item-icon fa-fw me-1"></i>Unit Converter
</a>
</li>
<li>
<a href="/exportData" id="LI51" class="dropdown-item">
<i class="far fa-download fa-fw me-1"></i>CSV Export
</a>
</li>
<li>
<a href="/balancecheck-tool" id="LI52" class="dropdown-item">
<i class="far fa-file-invoice-dollar fa-fw me-1"></i>Account Balance Checker
</a>
</li>
</ul>
</div>
<div class="col-sm py-5">
<h6 class="px-3 mb-3">Explore</h6>
<ul class="list-unstyled">
<li>
<a href="/gastracker" id="LI19" class="dropdown-item">
<i class="far fa-gas-pump dropdown-item-icon fa-fw me-1"></i>Gas Tracker
</a>
</li>
<li>
<a href="/dex" id="LI4" class="dropdown-item">
<i class="far fa-arrow-right-arrow-left dropdown-item-icon fa-fw me-1"></i>DEX Tracker
</a>
</li>
<li>
<a href="/nodetracker" id="LI46" class="dropdown-item">
<i class="far fa-server dropdown-item-icon fa-fw me-1"></i>Node Tracker
</a>
</li>
<li>
<a href="/labelcloud" id="LI41" class="dropdown-item">
<i class="far fa-signs-post dropdown-item-icon fa-fw me-1"></i>Label Cloud
</a>
</li>
<li>
<a href="/name-lookup" id="LI26" class="dropdown-item">
<i class="far fa-magnifying-glass-chart dropdown-item-icon fa-fw me-1"></i>Domain Name Lookup
</a>
</li>
</ul>
</div>
<div class="col-sm py-5">
<h6 class="px-3 mb-3">Services</h6>
<ul class="list-unstyled">
<li>
<a href="/tokenapprovalchecker" id="LI49" class="dropdown-item">
<i class="far fa-shield-keyhole dropdown-item-icon fa-fw me-1"></i>Token Approvals <span class="badge border bg-light text-muted">Beta</span>
</a>
</li>
<li>
<a href="/verifiedSignatures" id="LI29" class="dropdown-item">
<i class="far fa-signature-lock dropdown-item-icon fa-fw me-1"></i>Verified Signature
</a>
</li>
<li>
<a class="dropdown-item" href="/idm">
<i class="far fa-message-lines dropdown-item-icon fa-fw me-1"></i>Input Data Messages (IDM) <span class="badge border bg-light text-muted">Beta</span>
</a>
</li>
<li>
<a href="/advanced-filter" id="LI31" class="dropdown-item">
<i class="far fa-filters dropdown-item-icon fa-fw me-1"></i>Advanced Filter <span class="badge border bg-light text-muted">Beta</span>
</a>
</li>
<li>
<a class="dropdown-item" href="https://chat.blockscan.com" target="_blank">
<i class="far fa-messages dropdown-item-icon fa-fw me-1"></i>Blockscan Chat <i class="far fa-arrow-up-right-from-square text-muted ms-1"></i> <span class="badge border bg-light text-muted">Beta</span>
</a>
</li>
</ul>
</div>
</div>
</div>
</li>

<li class="nav-item dropdown d-block d-lg-none">
<a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">Explorers</a>
<ul class="dropdown-menu dropdown-menu-border" style="min-width: 14rem;">
<li>
<a href="https://etherscan.io" id="LI_Mainnet_1" class="dropdown-item active active">
Ethereum Mainnet
</a>
</li>
<li>
<a href="https://cn.etherscan.com/?lang=zh-CN" id="LI_Mainnet_CN_1" class="dropdown-item">
Ethereum Mainnet <span class="badge border bg-light text-dark ms-1">CN</span>
</a>
</li>
<li>
<a href="https://beaconscan.com/" id="LI77" class="dropdown-item">
Beaconscan <span class="badge border bg-light text-dark ms-1">ETH2</span>
</a>
</li>
<li>
<hr class="dropdown-divider">
</li>
<li>
<a href="https://goerli.etherscan.io" id="LI78" class="dropdown-item">
Goerli Testnet
</a>
</li>
<li>
<a href="https://sepolia.etherscan.io" id="LI79" class="dropdown-item">
Sepolia Testnet
</a>
</li>
<li>
<a href="https://holesky.etherscan.io" id="A4" class="dropdown-item">
Holesky Testnet
</a>
</li>
</ul>
</li>

<li class="nav-item dropdown d-block d-lg-none">
<a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">Appearance &amp; Settings</a>
<ul class="dropdown-menu dropdown-menu-border" style="min-width: 14rem;">
<li>
<button type="button" class="dropdown-item theme-btn active" data-bs-theme-value="light" onclick="setThemeMode('light');">
<i class="far fa-sun-bright fa-fw dropdown-item-icon theme-icon me-1" data-href="#fa-sun-bright"></i> Light
</button>
</li>
<li>
<button type="button" class="dropdown-item theme-btn" data-bs-theme-value="dim" onclick="setThemeMode('dim');">
<i class="far fa-moon-stars fa-fw dropdown-item-icon theme-icon me-1" data-href="#fa-moon-stars"></i> Dim
</button>
</li>
<li>
<button type="button" class="dropdown-item theme-btn" data-bs-theme-value="dark" onclick="setThemeMode('dark');">
<i class="far fa-moon-stars fa-fw dropdown-item-icon theme-icon me-1" data-href="#fa-moon"></i> Dark
</button>
</li>
<li>
<hr class="dropdown-divider">
</li>
<li>
<a class="dropdown-item" href="/settings">
<i class="far fa-gear fa-fw dropdown-item-icon me-1"></i> Site Settings <i class="far fa-arrow-right ms-1"></i>
</a>
</li>
</ul>
</li>

<li class="nav-item align-self-center d-none d-lg-block">
<span class="text-secondary">|</span>
</li>
<li class="nav-item dropdown">
<a class="nav-link dropdown-toggle" href="javascript:;" role="button" data-bs-toggle="dropdown" aria-expanded="false">
<i class="far fa-user-circle me-1"></i>SARTHAKM
</a>
<ul class="dropdown-menu dropdown-menu-border" style="min-width: 14rem; right: 0; left: auto;">
<li>
<a class="dropdown-item" href="/myaccount">
My Profile
</a>
</li>
<li>
<hr class="dropdown-divider">
</li>
<li>
<a class="dropdown-item" href="/myaddress">
Watch List
</a>
</li>
<li>
<a class="dropdown-item" href="/mynotes_tx">
Txn Private Notes
</a>
</li>
<li>
<a class="dropdown-item" href="/mynotes_address">
Private Name Tags
</a>
</li>
<li>
<a class="dropdown-item" href="/mytokenignore">
Token Ignore List
</a>
</li>
<li>
<hr class="dropdown-divider">
</li>
<li>
<a class="dropdown-item" href="/myapikey">
API Keys
</a>
</li>
<li>
<a class="dropdown-item" href="/myverify_address">
Verified Address
</a>
</li>
<li>
<a class="dropdown-item" href="/mycustomabi">
Custom ABI
</a>
</li>
<li>
<a class="dropdown-item" href="/myadvancedfilters">
Advanced Filter
</a>
</li>
<li>
<hr class="dropdown-divider">
</li>
<li>
<a class="btn btn-sm btn-soft-primary d-lg-block py-2 px-4" href="/login?cmd=logout">
<i class="far fa-sign-out me-1"></i> Sign Out
</a>
</li>
</ul>
</li>
</ul>
</div>
</div>
</nav>
</header>


<main id="content" class="main-content" role="main">
<input type="hidden" name="hdnAgeText" id="hdnAgeText" value="Age" />
<input type="hidden" name="hdnDateTimeText" id="hdnDateTimeText" value="Date Time (UTC)" />
<input type="hidden" name="hdnAgeTitle" id="hdnAgeTitle" value="Click to show Age Format" />
<input type="hidden" name="hdnDateTimeTitle" id="hdnDateTimeTitle" value="Click to show Datetime Format" />
<input type="hidden" name="hdnTxnText" id="hdnTxnText" value="Txn Fee" />
<input type="hidden" name="hdnGasPriceText" id="hdnGasPriceText" value="Gas Price" />
<input type="hidden" name="hdnTxnFeeTitle" id="hdnTxnFeeTitle" value="(Gas Price * Gas Used by Txns) in Ether" />
<input type="hidden" name="hdnGasPriceTitle" id="hdnGasPriceTitle" value="Gas Price in Gwei" />

<section class="container-xxl">
<div class="d-flex flex-wrap justify-content-between align-items-center border-bottom gap-3 py-5">
<h1 class="h5 mb-0">
Accounts&nbsp;
<span class="small text-muted">
Armor.fi
</span>
</h1>
</div>
</section>


<section class="container-xxl">
<div class="text-muted py-3">
<span id="ContentPlaceHolder1_lblAdResult"><ins data-revive-zoneid="2" data-revive-id="6452186c83cd256052c3c100f524ed97"></ins><script async src="//kta.etherscan.com/www/d/asyncjses.php?v=0.01"></script></span>&nbsp;
</div>
</section>


<section class="container-xxl pt-5 pb-12">

<div class="d-flex align-items-center gap-2 mb-3"><span class="fw-bold">Related labels </span><a class="btn btn-sm btn-secondary rounded-pill" href="/tokens/label/armor-fi">Token (1)</a></div>


<div class="card p-4 mb-2"><div class="d-flex align-items-basline gap-3"><i class="far fa-sparkles fs-5"></i><div>&lt;p&gt;Armor is a smart insurance aggregator for DeFi, built on trustless and decentralized financial infrastructure.&lt;/p&gt;
</div></div></div>


<div class="card">




<div class="tab-content" id="tabContent"><div class="tab-pane fade show active" id="subcattab-0" role="tabpanel" aria-labelledby="0-tab"><div class="table-responsive " id="paywall_mask_table-subcatid-0"><table class="table table-hover table-align-middle mb-0" style="width:100%" id="table-subcatid-0"><thead class="align-middle text-nowrap"><tr><th scope="col" width="370">Address</th><th class="remove-icon" scope="col">Name Tag</th><th scope="col"> Balance</th><th scope="col"> Txn Count</th></tr></thead><tbody><tr class="odd"><td class="align-items-center"><span class="d-flex align-items-center"><span class="d-flex align-items-center" style="white-space:nowrap;"><i data-bs-toggle="tooltip" title="Contract" class="far fa-file-alt text-secondary me-1"></i><a class="me-1" href="/address/0xd7b8ef47c08f824cea3d837afa61484e81d14bfb" data-bs-toggle="tooltip" data-bs-title="0xd7b8ef47c08f824cea3d837afa61484e81d14bfb"><span data-highlight-target="0xD7b8Ef47C08F824ceA3d837afA61484e81d14BfB">0xD7b8Ef...81d14BfB</span></a> <a class="js-clipboard link-secondary  " href="javascript:;" data-clipboard-text="0xD7b8Ef47C08F824ceA3d837afA61484e81d14BfB" data-bs-toggle="tooltip" data-bs-trigger="hover" title="Copy Address" data-hs-clipboard-options="{ &quot;type&quot;: &quot;tooltip&quot;, &quot;successText&quot;: &quot;Copied!&quot;, &quot;classChangeTarget&quot;: &quot;#linkIcon_0xd7b_1&quot;, &quot;defaultClass&quot;: &quot;fa-copy&quot;, &quot;successClass&quot;: &quot;fa-check&quot; }"><i id="linkIcon_0xd7b_1" class="far fa-copy fa-fw"></i> </a></span></span></td><td>Armor.fi: ARMOR/DAI 1inch LP</td><td>0 ETH</td><td>414</td></tr><tr class="even"><td class="align-items-center"><span class="d-flex align-items-center"><span class="d-flex align-items-center" style="white-space:nowrap;"><i data-bs-toggle="tooltip" title="Contract" class="far fa-file-alt text-secondary me-1"></i><a class="me-1" href="/address/0xa659e66e116d354e779d8dbb35319af67171ffb4" data-bs-toggle="tooltip" data-bs-title="0xa659e66e116d354e779d8dbb35319af67171ffb4"><span data-highlight-target="0xa659e66E116D354e779D8dbb35319AF67171ffb4">0xa659e6...7171ffb4</span></a> <a class="js-clipboard link-secondary  " href="javascript:;" data-clipboard-text="0xa659e66E116D354e779D8dbb35319AF67171ffb4" data-bs-toggle="tooltip" data-bs-trigger="hover" title="Copy Address" data-hs-clipboard-options="{ &quot;type&quot;: &quot;tooltip&quot;, &quot;successText&quot;: &quot;Copied!&quot;, &quot;classChangeTarget&quot;: &quot;#linkIcon_0xa65_2&quot;, &quot;defaultClass&quot;: &quot;fa-copy&quot;, &quot;successClass&quot;: &quot;fa-check&quot; }"><i id="linkIcon_0xa65_2" class="far fa-copy fa-fw"></i> </a></span></span></td><td>Armor.fi: ARMOR/DAI Uni LP</td><td>0 ETH</td><td>1,162</td></tr><tr class="odd"><td class="align-items-center"><span class="d-flex align-items-center"><span class="d-flex align-items-center" style="white-space:nowrap;"><i data-bs-toggle="tooltip" title="Contract" class="far fa-file-alt text-secondary me-1"></i><a class="me-1" href="/address/0x01acad2228f18598cd2b8611acd37992bf27313c" data-bs-toggle="tooltip" data-bs-title="0x01acad2228f18598cd2b8611acd37992bf27313c"><span data-highlight-target="0x01Acad2228F18598CD2b8611aCD37992BF27313C">0x01Acad...BF27313C</span></a> <a class="js-clipboard link-secondary  " href="javascript:;" data-clipboard-text="0x01Acad2228F18598CD2b8611aCD37992BF27313C" data-bs-toggle="tooltip" data-bs-trigger="hover" title="Copy Address" data-hs-clipboard-options="{ &quot;type&quot;: &quot;tooltip&quot;, &quot;successText&quot;: &quot;Copied!&quot;, &quot;classChangeTarget&quot;: &quot;#linkIcon_0x01a_3&quot;, &quot;defaultClass&quot;: &quot;fa-copy&quot;, &quot;successClass&quot;: &quot;fa-check&quot; }"><i id="linkIcon_0x01a_3" class="far fa-copy fa-fw"></i> </a></span></span></td><td>Armor.fi: ARMOR/WBTC Uni LP</td><td>0 ETH</td><td>653</td></tr><tr class="even"><td class="align-items-center"><span class="d-flex align-items-center"><span class="d-flex align-items-center" style="white-space:nowrap;"><i data-bs-toggle="tooltip" title="Contract" class="far fa-file-alt text-secondary me-1"></i><a class="me-1" href="/address/0xf991f1e1b8acd657661c89b5cd452d86de76a8c1" data-bs-toggle="tooltip" data-bs-title="0xf991f1e1b8acd657661c89b5cd452d86de76a8c1"><span data-highlight-target="0xf991f1e1B8Acd657661c89b5CD452d86De76a8C1">0xf991f1...De76a8C1</span></a> <a class="js-clipboard link-secondary  " href="javascript:;" data-clipboard-text="0xf991f1e1B8Acd657661c89b5CD452d86De76a8C1" data-bs-toggle="tooltip" data-bs-trigger="hover" title="Copy Address" data-hs-clipboard-options="{ &quot;type&quot;: &quot;tooltip&quot;, &quot;successText&quot;: &quot;Copied!&quot;, &quot;classChangeTarget&quot;: &quot;#linkIcon_0xf99_4&quot;, &quot;defaultClass&quot;: &quot;fa-copy&quot;, &quot;successClass&quot;: &quot;fa-check&quot; }"><i id="linkIcon_0xf99_4" class="far fa-copy fa-fw"></i> </a></span></span></td><td>Armor.fi: ARMOR/WETH Uni LP</td><td>0 ETH</td><td>4,344</td></tr><tr class="odd"><td class="align-items-center"><span class="d-flex align-items-center"><span class="d-flex align-items-center" style="white-space:nowrap;"><i data-bs-toggle="tooltip" title="Contract" class="far fa-file-alt text-secondary me-1"></i><a class="me-1" href="/address/0x1337def1670c54b2a70e590b5654c2b7ce1141a2" data-bs-toggle="tooltip" data-bs-title="0x1337def1670c54b2a70e590b5654c2b7ce1141a2"><span data-highlight-target="0x1337DEF1670C54B2a70E590B5654c2B7cE1141a2">0x1337DE...cE1141a2</span></a> <a class="js-clipboard link-secondary  " href="javascript:;" data-clipboard-text="0x1337DEF1670C54B2a70E590B5654c2B7cE1141a2" data-bs-toggle="tooltip" data-bs-trigger="hover" title="Copy Address" data-hs-clipboard-options="{ &quot;type&quot;: &quot;tooltip&quot;, &quot;successText&quot;: &quot;Copied!&quot;, &quot;classChangeTarget&quot;: &quot;#linkIcon_0x133_5&quot;, &quot;defaultClass&quot;: &quot;fa-copy&quot;, &quot;successClass&quot;: &quot;fa-check&quot; }"><i id="linkIcon_0x133_5" class="far fa-copy fa-fw"></i> </a></span></span></td><td>Armor.fi: arNFT Staking Contract</td><td>0 ETH</td><td>731</td></tr><tr class="even"><td class="align-items-center"><span class="d-flex align-items-center"><span class="d-flex align-items-center" style="white-space:nowrap;"><i data-bs-toggle="tooltip" title="Contract" class="far fa-file-alt text-secondary me-1"></i><a class="me-1" href="/address/0xfdf5709d44b26a7dd112556dd1b1ce53c0eaf454" data-bs-toggle="tooltip" data-bs-title="0xfdf5709d44b26a7dd112556dd1b1ce53c0eaf454"><span data-highlight-target="0xfDF5709D44b26A7DD112556Dd1B1cE53c0eAF454">0xfDF570...c0eAF454</span></a> <a class="js-clipboard link-secondary  " href="javascript:;" data-clipboard-text="0xfDF5709D44b26A7DD112556Dd1B1cE53c0eAF454" data-bs-toggle="tooltip" data-bs-trigger="hover" title="Copy Address" data-hs-clipboard-options="{ &quot;type&quot;: &quot;tooltip&quot;, &quot;successText&quot;: &quot;Copied!&quot;, &quot;classChangeTarget&quot;: &quot;#linkIcon_0xfdf_6&quot;, &quot;defaultClass&quot;: &quot;fa-copy&quot;, &quot;successClass&quot;: &quot;fa-check&quot; }"><i id="linkIcon_0xfdf_6" class="far fa-copy fa-fw"></i> </a></span></span></td><td>Armor.fi: ETH/ARMOR 1inch LP</td><td>0 ETH</td><td>630</td></tr><tr class="odd"><td class="align-items-center"><span class="d-flex align-items-center"><span class="d-flex align-items-center" style="white-space:nowrap;"><i data-bs-toggle="tooltip" title="Contract" class="far fa-file-alt text-secondary me-1"></i><a class="me-1" href="/address/0x1337def159da6f97db7c4d0e257dc689837b9e70" data-bs-toggle="tooltip" data-bs-title="0x1337def159da6f97db7c4d0e257dc689837b9e70"><span data-highlight-target="0x1337DEF159da6F97dB7c4D0E257dc689837b9E70">0x1337DE...837b9E70</span></a> <a class="js-clipboard link-secondary  " href="javascript:;" data-clipboard-text="0x1337DEF159da6F97dB7c4D0E257dc689837b9E70" data-bs-toggle="tooltip" data-bs-trigger="hover" title="Copy Address" data-hs-clipboard-options="{ &quot;type&quot;: &quot;tooltip&quot;, &quot;successText&quot;: &quot;Copied!&quot;, &quot;classChangeTarget&quot;: &quot;#linkIcon_0x133_7&quot;, &quot;defaultClass&quot;: &quot;fa-copy&quot;, &quot;successClass&quot;: &quot;fa-check&quot; }"><i id="linkIcon_0x133_7" class="far fa-copy fa-fw"></i> </a></span></span></td><td>Armor.fi: FarmController</td><td>0 ETH</td><td>84</td></tr><tr class="even"><td class="align-items-center"><span class="d-flex align-items-center"><span class="d-flex align-items-center" style="white-space:nowrap;"><i data-bs-toggle="tooltip" title="Contract" class="far fa-file-alt text-secondary me-1"></i><a class="me-1" href="/address/0x0bdb7976c34ab05e5a9031f258b8956f68ee29cf" data-bs-toggle="tooltip" data-bs-title="0x0bdb7976c34ab05e5a9031f258b8956f68ee29cf"><span data-highlight-target="0x0Bdb7976c34aB05E5a9031F258B8956f68ee29cf">0x0Bdb79...68ee29cf</span></a> <a class="js-clipboard link-secondary  " href="javascript:;" data-clipboard-text="0x0Bdb7976c34aB05E5a9031F258B8956f68ee29cf" data-bs-toggle="tooltip" data-bs-trigger="hover" title="Copy Address" data-hs-clipboard-options="{ &quot;type&quot;: &quot;tooltip&quot;, &quot;successText&quot;: &quot;Copied!&quot;, &quot;classChangeTarget&quot;: &quot;#linkIcon_0x0bd_8&quot;, &quot;defaultClass&quot;: &quot;fa-copy&quot;, &quot;successClass&quot;: &quot;fa-check&quot; }"><i id="linkIcon_0x0bd_8" class="far fa-copy fa-fw"></i> </a></span></span></td><td>Armor.fi: FarmController Master</td><td>0 ETH</td><td>2</td></tr><tr class="odd"><td class="align-items-center"><span class="d-flex align-items-center"><span class="d-flex align-items-center" style="white-space:nowrap;"><i data-bs-toggle="tooltip" title="Contract" class="far fa-file-alt text-secondary me-1"></i><a class="me-1" href="/address/0x1f28ed9d4792a567dad779235c2b766ab84d8e33" data-bs-toggle="tooltip" data-bs-title="0x1f28ed9d4792a567dad779235c2b766ab84d8e33"><span data-highlight-target="0x1f28eD9D4792a567DaD779235c2b766Ab84D8E33">0x1f28eD...b84D8E33</span></a> <a class="js-clipboard link-secondary  " href="javascript:;" data-clipboard-text="0x1f28eD9D4792a567DaD779235c2b766Ab84D8E33" data-bs-toggle="tooltip" data-bs-trigger="hover" title="Copy Address" data-hs-clipboard-options="{ &quot;type&quot;: &quot;tooltip&quot;, &quot;successText&quot;: &quot;Copied!&quot;, &quot;classChangeTarget&quot;: &quot;#linkIcon_0x1f2_9&quot;, &quot;defaultClass&quot;: &quot;fa-copy&quot;, &quot;successClass&quot;: &quot;fa-check&quot; }"><i id="linkIcon_0x1f2_9" class="far fa-copy fa-fw"></i> </a></span></span></td><td>Armor.fi: MultiSig</td><td>2<b>.</b>58212203 ETH</td><td>1,043</td></tr><tr class="even"><td class="align-items-center"><span class="d-flex align-items-center"><span class="d-flex align-items-center" style="white-space:nowrap;"><i data-bs-toggle="tooltip" title="Contract" class="far fa-file-alt text-secondary me-1"></i><a class="me-1" href="/address/0xeff1cdc3cc01afab104b00a7d9cd09619b94ae8f" data-bs-toggle="tooltip" data-bs-title="0xeff1cdc3cc01afab104b00a7d9cd09619b94ae8f"><span data-highlight-target="0xefF1CDc3CC01afAB104b00a7D9cd09619B94ae8F">0xefF1CD...9B94ae8F</span></a> <a class="js-clipboard link-secondary  " href="javascript:;" data-clipboard-text="0xefF1CDc3CC01afAB104b00a7D9cd09619B94ae8F" data-bs-toggle="tooltip" data-bs-trigger="hover" title="Copy Address" data-hs-clipboard-options="{ &quot;type&quot;: &quot;tooltip&quot;, &quot;successText&quot;: &quot;Copied!&quot;, &quot;classChangeTarget&quot;: &quot;#linkIcon_0xeff_10&quot;, &quot;defaultClass&quot;: &quot;fa-copy&quot;, &quot;successClass&quot;: &quot;fa-check&quot; }"><i id="linkIcon_0xeff_10" class="far fa-copy fa-fw"></i> </a></span></span></td><td>Armor.fi: Referral Rewards Master</td><td>0 ETH</td><td>2</td></tr><tr class="odd"><td class="align-items-center"><span class="d-flex align-items-center"><span class="d-flex align-items-center" style="white-space:nowrap;"><i data-bs-toggle="tooltip" title="Contract" class="far fa-file-alt text-secondary me-1"></i><a class="me-1" href="/address/0x1337def1c79053da23921a3634adbd12f3b748a5" data-bs-toggle="tooltip" data-bs-title="0x1337def1c79053da23921a3634adbd12f3b748a5"><span data-highlight-target="0x1337DEF1C79053dA23921a3634aDbD12f3b748A5">0x1337DE...f3b748A5</span></a> <a class="js-clipboard link-secondary  " href="javascript:;" data-clipboard-text="0x1337DEF1C79053dA23921a3634aDbD12f3b748A5" data-bs-toggle="tooltip" data-bs-trigger="hover" title="Copy Address" data-hs-clipboard-options="{ &quot;type&quot;: &quot;tooltip&quot;, &quot;successText&quot;: &quot;Copied!&quot;, &quot;classChangeTarget&quot;: &quot;#linkIcon_0x133_11&quot;, &quot;defaultClass&quot;: &quot;fa-copy&quot;, &quot;successClass&quot;: &quot;fa-check&quot; }"><i id="linkIcon_0x133_11" class="far fa-copy fa-fw"></i> </a></span></span></td><td>Armor.fi: Referral Rewards Proxy</td><td>0 ETH</td><td>20</td></tr><tr class="even"><td class="align-items-center"><span class="d-flex align-items-center"><span class="d-flex align-items-center" style="white-space:nowrap;"><i data-bs-toggle="tooltip" title="Contract" class="far fa-file-alt text-secondary me-1"></i><a class="me-1" href="/address/0x1337def1b1ae35314b40e5a4b70e216a499b0e37" data-bs-toggle="tooltip" data-bs-title="0x1337def1b1ae35314b40e5a4b70e216a499b0e37"><span data-highlight-target="0x1337DEF1B1Ae35314b40e5A4b70e216A499b0E37">0x1337DE...499b0E37</span></a> <a class="js-clipboard link-secondary  " href="javascript:;" data-clipboard-text="0x1337DEF1B1Ae35314b40e5A4b70e216A499b0E37" data-bs-toggle="tooltip" data-bs-trigger="hover" title="Copy Address" data-hs-clipboard-options="{ &quot;type&quot;: &quot;tooltip&quot;, &quot;successText&quot;: &quot;Copied!&quot;, &quot;classChangeTarget&quot;: &quot;#linkIcon_0x133_12&quot;, &quot;defaultClass&quot;: &quot;fa-copy&quot;, &quot;successClass&quot;: &quot;fa-check&quot; }"><i id="linkIcon_0x133_12" class="far fa-copy fa-fw"></i> </a></span></span></td><td>Armor.fi: Rewards Vault</td><td>0 ETH</td><td>1,908</td></tr><tr class="odd"><td class="align-items-center"><span class="d-flex align-items-center"><span class="d-flex align-items-center" style="white-space:nowrap;"><i data-bs-toggle="tooltip" title="Contract" class="far fa-file-alt text-secondary me-1"></i><a class="me-1" href="/address/0x1337def11d788e62a253fea846a505ee1b57623f" data-bs-toggle="tooltip" data-bs-title="0x1337def11d788e62a253fea846a505ee1b57623f"><span data-highlight-target="0x1337DEF11D788e62A253feA846A505EE1b57623f">0x1337DE...1b57623f</span></a> <a class="js-clipboard link-secondary  " href="javascript:;" data-clipboard-text="0x1337DEF11D788e62A253feA846A505EE1b57623f" data-bs-toggle="tooltip" data-bs-trigger="hover" title="Copy Address" data-hs-clipboard-options="{ &quot;type&quot;: &quot;tooltip&quot;, &quot;successText&quot;: &quot;Copied!&quot;, &quot;classChangeTarget&quot;: &quot;#linkIcon_0x133_13&quot;, &quot;defaultClass&quot;: &quot;fa-copy&quot;, &quot;successClass&quot;: &quot;fa-check&quot; }"><i id="linkIcon_0x133_13" class="far fa-copy fa-fw"></i> </a></span></span></td><td>Armor.fi: Timelock</td><td>0 ETH</td><td>15</td></tr></tbody><tfoot id="sublabel-0"><tr class="table-active"><th class="border-top border-bottom-0"></th><th class="border-top border-bottom-0">Sum of 13 Accounts</th><th class="border-top border-bottom-0">2.58212203 Ether</th><th class="border-top border-bottom-0">11,008</th></tr></tfoot></table></div></div></div>

<form method="post" action="./armor-fi" id="frmTblFooter">
<div class="aspNetHidden">
<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="LSxoGMWyFLsmbxPLfITejbZA1FpUy6UZFs14Zf0guriQVuDJiz39s8Za/fa8hXwmmGwNRYPgRVtqMg1WN662R3mpFI9IHwbBxSmH5Y7+6v4=" />
</div>
<div class="aspNetHidden">
<input type="hidden" name="__VIEWSTATEGENERATOR" id="__VIEWSTATEGENERATOR" value="A75D1253" />
</div>
<script type="text/javascript">
//<![CDATA[
$('#spinwheel').remove();//]]>
</script>
</form>

</div>




<div id="ContentPlaceHolder1_divFootNote" class="mt-4">
<p class="d-flex align-items-baseline fs-sm text-muted gap-1 mb-3"><i class="far fa-lightbulb-on"></i><span>Note : Labels source attribution required if used externally</span></p>
</div>

</section>

<input type="hidden" id="hdnLabelFilter" value="armor-fi">
<script>
        var mydt = []
        var resetSortAfterClickDictionary = {};
        var resetSortDictionary = {};
        var resetPageDictionary = {};
        var visitedTabDictionary = {};
        var queryStringDictionary = {};
        var currentLengthDictionary = {};
        var currentTab = '0'
            var refreshToDefaultDictionary = {'table-subcatid-0': false};
            var defaultLength = 25
            var defaultSort = { column: 1, dir: 'asc' }

        function updateUrl(subCatId) {
            var queryString = '';
            queryString += 'subcatid=' + subCatId;

            var length = queryStringDictionary["length_" + subCatId];
            if (length) {
                if (length < 0) {
                    length = 7
                }
                queryString += "&size=" + length;
            }

            var start = queryStringDictionary["start_" + subCatId];
            if (start !== undefined) {
                queryString += "&start=" + start;
            }

            var col = queryStringDictionary["col_" + subCatId];
            if (col !== undefined) {
                queryString += "&col=" + col;
            }

            var order = queryStringDictionary["order_" + subCatId];
            if (order !== undefined) {
                queryString += "&order=" + order;
            }

            var baseUrl = window.location.href.split('?')[0];
            history.pushState("", document.title, baseUrl + "?" + queryString);
        }

        function selectTab(el) {
          
            $('.nav-link.active#tab-xx').removeClass("active");
            el.classList.add("active");

            var id = $('.nav-link.active#tab-xx').attr('val');
            $("#subcattab-" + currentTab).removeClass("show").removeClass("active");

            $("#subcattab-" + id).addClass("show").addClass("active");

            if (!visitedTabDictionary["subCat_" + id]) {
                visitedTabDictionary["subCat_" + id] = true;
                $('#table-subcatid-' + id).DataTable().ajax.reload();
            }

            updateUrl(id);
            currentTab = id;

            //show correct footer
            var subCategoryId = $('.nav-link.active#tab-xx').attr('val');
            $('tfoot[class!="hideFooter"]').addClass('hideFooter');
            $('#sublabel-' + subCategoryId.toString()).removeClass('hideFooter');

        }

        function generateLabelModel() {
            var id = $('#hdnId').val();
            var label = $('#hdnLabelFilter').val();
            var subCategoryId = $('.nav-link.active#tab-xx').attr('val');

            return { id: id, label: label, subCategoryId: subCategoryId };
        }

        $(document).ready(function () {

            visitedTabDictionary["subCat_" + currentTab] = true;
            resetSortAfterClickDictionary["table-subcatid-" + currentTab] = false;

            var config = {
                dom: '<"top d-flex flex-column flex-sm-row justify-content-between gap-3 p-3 topdivdt"<"text-muted datainfo"i>>rt<"card-footer d-flex flex-wrap justify-content-between align-items-center gap-3 bottomdivdt"<"d-flex align-items-center gap-2"l><p>><"clear">',
                language: {
                    paginate: {
                        next: '<i class="fa fa-chevron-right small"></i>',
                        previous: '<i class="fa fa-chevron-left small"></i>'
                    },
                    lengthMenu: "Show rows: _MENU_",
                    info: "A total of _MAX_ accounts found"
                },
                searching: false,
                pagingType: 'full',
                order: [[1,'asc']],
                columnDefs: [
                    { orderable: true, targets: 2, orderSequence: ["desc", "asc", "reset"] },
                    { orderable: true, targets: 3, orderSequence: ["desc", "asc", "reset"] },
                    { orderable: false, targets: '_all' }
                ],
                
                processing: true,
                serverSide: true,
                
                pageLength: 25,
                displayStart:0,
                deferLoading: 13,
                ajax: {
                    type: "POST",
                    contentType: "application/json",
                    url: "/accounts.aspx/GetTableEntriesBySubLabel",
                    data: function (d, settings) {
                        // note: d is created by datatable, the structure of d is the same with DataTableParameters model above
                        var labelModel = generateLabelModel();

                        if (refreshToDefaultDictionary[settings.nTable.getAttribute("id")]) {
                            d.length = defaultLength;
                            d.order[0] = defaultSort;
                        }

                        if (currentLengthDictionary[settings.nTable.getAttribute("id")] != d.length) {
                            if (currentLengthDictionary[settings.nTable.getAttribute("id")] != undefined) {
                                d.start = 0;
                                resetPageDictionary[settings.nTable.getAttribute("id")] = true;
                            }
                            currentLengthDictionary[settings.nTable.getAttribute("id")] = d.length;
                        }

                        if ((d.order[0] && d.order[0].dir === "reset") ||
                            resetSortAfterClickDictionary[settings.nTable.getAttribute("id")]) {
                            d.order[0] = { column: 1, dir: "desc" }
                            resetSortDictionary[settings.nTable.getAttribute("id")] = true;
                        }
                        else {
                            resetSortDictionary[settings.nTable.getAttribute("id")] = false;
                        }
                        return JSON.stringify({ dataTableModel: d, labelModel: labelModel });
                    },
                    dataType: 'json',
                    dataFilter: function (res) {
                        var parsed = JSON.parse(res);
                        var morp = parsed.d;
                        return JSON.stringify(morp);
                    }
                },
                columns: [
                    { data: "address" },
                    { data: "nameTag" },
                    { data: "balance" },
                    { data: "txnCount" }
                ],                
                drawCallback: function(settings) {

                    //change sorting icon and position
                    $("#" + this.attr('id') + " th.sorting_asc").not(".remove-icon").each(function () {
                        var text = $(this).text();
                        text = '<i class="fad fa-sort-up"></i>' + text;
                        $(this).html(text);
                    });

                    $("#" + this.attr('id') + " th.sorting_desc").not(".remove-icon").each(function () {
                        var text = $(this).text();
                        text = '<i class="fad fa-sort-down"></i>' + text;
                        $(this).html(text);
                    });

                    $("#" + this.attr('id') + " th.sorting").not(".remove-icon").each(function () {
                        var text = $(this).text();
                        text = '<i class="fad fa-sort"></i>' + text;
                        $(this).html(text);
                    });

                    var api = this.api();
                    var json = api.ajax.json();
                    if (!json) {
                        var currentPageDisp = "1";

                        //reload state if querystring is available
                        var urlParams = new URLSearchParams(window.location.search);
                        var existLength = urlParams.get('size');
                        if (existLength) {
                            api.page.len(existLength);
                            currentLengthDictionary[this.attr('id')] = parseInt(existLength)

                            var existStart = urlParams.get('start');
                            if (!existStart) {
                                existStart = 0
                            }
                            currentPage = Math.floor(existStart / existLength);
                            api.page(currentPage);
                            currentPageDisp = currentPage + 1;
                        }

                        var existCol = urlParams.get('col');
                        var existOrder = urlParams.get('order');

                        if (existCol && existOrder) {
                            this.api().order([parseInt(existCol), existOrder]);
                        }

                        $('.custom-select.custom-select-sm.form-control.form-control-sm').removeAttr("class").addClass("form-select form-select-sm w-auto");
                        var totalPage = 1;
                        $('#' + this.attr('id') + '_wrapper .paginate_button.previous').after("<li class='page-item disabled'><span class='page-link'>Page " + currentPageDisp + " of " + totalPage + "</span></li>");
                        
                        $(".previous a").addClass("px-3");
                        $(".next a").addClass("px-3");
                        var dataInfoDiv = document.getElementsByClassName("datainfo");
                        $("#divDataInfo").append(dataInfoDiv);
                        $(".dataTables_length").find("label").addClass("d-flex align-items-center gap-2 text-muted");
                        $('[data-bs-toggle="tooltip"]').tooltip();
                        HSCore.components.HSClipboard.init('.js-clipboard');
                        return;
                    } else {
                        $('#' + this.attr('id') + '_wrapper .paginate_button.previous').after("<li class='page-item disabled'><span class='page-link'>Page " + json.currentPage + " of " + json.totalPage + "</span></li>");
                        
                        $(".previous a").addClass("px-3");
                        $(".next a").addClass("px-3");
                        var dataInfoDiv = document.getElementsByClassName("datainfo");
                        $("#divDataInfo").append(dataInfoDiv);
                        $(".dataTables_length").find("label").addClass("d-flex align-items-center gap-2 text-muted");
                        $(".pagination").addClass("pagination-sm mb-0");
                        $('[data-bs-toggle="tooltip"]').tooltip();
                        HSCore.components.HSClipboard.init('.js-clipboard');

                        if (refreshToDefaultDictionary[settings.nTable.getAttribute("id")]) {
                            refreshToDefaultDictionary[settings.nTable.getAttribute("id")] = false;
                            this.api().page.len(defaultLength);
                            this.api().order([defaultSort["column"], defaultSort["dir"]]);
                            $("#" + this.attr('id') + " .default-sort").not("no-login").removeClass("sorting").addClass("sorting_desc")
                            $("#" + this.attr('id') + " .sorting_desc").not(".default-sort").removeClass("sorting_desc").addClass("sorting").removeAttr("aria-sort");
                            $("#" + this.attr('id') + " .sorting_asc").not(".default-sort").removeClass("sorting_asc").addClass("sorting").removeAttr("aria-sort");
                        }

                        //bypass standard datatables sorting selection
                        if (resetSortDictionary[this.attr('id')] || resetSortAfterClickDictionary[this.attr('id')]) {
                            this.api().order([1, 'desc']); //the default sorting is column 3
                            resetSortAfterClickDictionary[this.attr('id')] = false;
                            $("#" + this.attr('id') + " .default-sort").not("no-login").removeClass("sorting").addClass("sorting_desc")
                            $("#" + this.attr('id') + " .sorting_desc").not(".default-sort").removeClass("sorting_desc").addClass("sorting").removeAttr("aria-sort");
                            $("#" + this.attr('id') + " .sorting_asc").not(".default-sort").removeClass("sorting_asc").addClass("sorting").removeAttr("aria-sort");
                        }

                        if (resetPageDictionary[this.attr('id')]) {
                            this.api().page(0);
                            resetPageDictionary[this.attr('id')] = false;
                        }

                        $("#" + this.attr('id') + " th.sorting_asc").not(".remove-icon").each(function () {
                            var text = $(this).text();
                            text = '<i class="fad fa-sort-up"></i> ' + text;
                            $(this).html(text);
                        });

                        $("#" + this.attr('id') + " th.sorting_desc").not(".remove-icon").each(function () {
                            var text = $(this).text();
                            text = '<i class="fad fa-sort-down"></i> ' + text;
                            $(this).html(text);
                        });

                        $("#" + this.attr('id') + " th.sorting").not(".remove-icon").each(function () {
                            var text = $(this).text();
                            text = '<i class="fad fa-sort"></i> ' + text;
                            $(this).html(text);
                        });
                    }

                    var subCatId = $('.nav-link.active#tab-xx').attr('val');

                    //get page info
                    var pageInfo = this.api().page.info();

                    if (pageInfo.length) {
                        queryStringDictionary["length_" + subCatId] = pageInfo.length;
                    }

                    if (pageInfo.start !== undefined) {
                        queryStringDictionary["start_" + subCatId] = pageInfo.start;
                    }

                    //get ordering info
                    var orderInfo = this.api().order();
                    queryStringDictionary["col_" + subCatId] = orderInfo[0][0];
                    queryStringDictionary["order_" + subCatId] = orderInfo[0][1];

                    if (mydt[this.attr('id') ]) {
                        mydt[this.attr('id') ].columns.adjust();
                    }
                    updateUrl(subCatId);
                    $('[data-bs-toggle="tooltip"]').tooltip();
                }, initComplete: function (settings, json) {
                    $(".pagination").addClass("pagination-sm mb-0");
                    if (mydt[this.attr('id')]) {
                        mydt[this.attr('id')].columns.adjust();
                    }
                },
        }
        mydt['table-subcatid-0'] = $('#table-subcatid-0').DataTable(config);
    });
    </script>
</main>
<div id="push" style="display: none;"></div>
<div class="modal fade" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" id="emailSubscribeModalBox" aria-hidden="true">
<div class="modal-dialog modal-sm" role="document">
<div class="modal-content">
<div class="modal-body">
<button type="button" class="close close-md" data-bs-dismiss="modal" aria-label="Close">
<span aria-hidden="true">&times;</span>
</button>
<div class="text-center py-5-alt px-4">
<div id="emailSubscribeModalBoxText"></div>
</div>
</div>
</div>
</div>
</div>
<div class="modal fade" id="copyAddressConfirmModal" tabindex="-1" role="dialog">
<div class="modal-dialog modal-md">
<div class="modal-content">
<div class="modal-header border-0">
<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
</div>
<div class="modal-body pt-0">
<div class="mb-5">
<div class="text-center">
<div class="mb-2">
<i class="fas fa-exclamation-triangle text-warning fs-2"></i>
</div>
<h6 class="modal-title fs-5 mb-0">Before You Copy</h6>
</div>
<div class="mb-3 text-center">
<p class="text-muted small" id="addressToCopy"></p>
</div>
<p id="copyAddressConfirmMessage"></p>
<div class="form-check">
<input class="form-check-input" type="checkbox" value id="popupDontShowAgain">
<label class="form-check-label" for="popupDontShowAgain">Don't show this for 30 days</label>
</div>
</div>
<div class="text-center">
<button type="button" id="btnConfirmCopyAddress" data-clipboard-target="#addressToCopy" class="btn btn-lg btn-secondary" data-bs-dismiss="modal">
Understand, Copy Address
</button>
</div>
</div>
</div>
</div>
</div>
<footer id="masterFooter" class="bg-light mt-auto d-print-none">
<div class="container-xxl">
<div class="d-flex justify-content-between align-items-baseline py-6">

<div class="d-flex gap-2">
<a class="btn btn-sm btn-secondary content-center rounded-circle" style="width: 2rem; height: 2rem;" href="https://twitter.com/etherscan" rel="nofollow noopener" target="_blank" data-bs-toggle="tooltip" data-bs-trigger="hover" data-bs-placement="top" title="Twitter">
<i class="fab fa-twitter"></i>
</a>
<a class="btn btn-sm btn-secondary content-center rounded-circle" style="width: 2rem; height: 2rem;" href="https://medium.com/etherscan-blog" rel="nofollow noopener" target="_blank" data-bs-toggle="tooltip" data-bs-trigger="hover" data-bs-placement="top" title="Medium">
<i class="fab fa-medium"></i>
</a>
<a class="btn btn-sm btn-secondary content-center rounded-circle" style="width: 2rem; height: 2rem;" href="https://www.facebook.com/etherscan/" rel="nofollow noopener" target="_blank" data-bs-toggle="tooltip" data-bs-trigger="hover" data-bs-placement="top" title="Facebook">
<i class="fab fa-facebook"></i>
</a>
<a class="btn btn-sm btn-secondary content-center rounded-circle" style="width: 2rem; height: 2rem;" href="https://www.reddit.com/r/etherscan/" rel="nofollow noopener" target="_blank" data-bs-toggle="tooltip" data-bs-trigger="hover" data-bs-placement="top" title="Reddit">
<i class="fab fa-reddit-alien"></i>
</a>
</div>

<a class="link-dark" href="#">
<i class="far fa-arrow-up-to-line me-1"></i>Back to Top
</a>
</div>
<hr class="my-0">

<div class="row justify-content-md-between py-8 py-lg-10">
<div class="col-lg-4 pe-xl-16 mb-4 mb-lg-0">
<div class="d-flex align-items-center mb-3">
<img class="me-2" width="20" data-img-theme="light" src="/images/svg/brands/ethereum-original.svg" alt="Ethereum Logo">
<img class="me-2" width="20" data-img-theme="darkmode" src="/images/svg/brands/ethereum-original-light.svg" alt="Ethereum Logo">
<span class="fs-5">Powered by Ethereum</span>
</div>
<p class="fs-sm">Etherscan is a Block Explorer and Analytics Platform for Ethereum, a decentralized smart contracts platform.</p>
<div class="d-none d-lg-block mt-n4 mb-n6">
<img class="opacity-50" width="280" data-img-theme="light" src="/images/map.png" alt="Background Map Image">
<img class="opacity-50" width="280" data-img-theme="darkmode" src="/images/map-light.png" alt="Background Map Image">
</div>
</div>
<div class="col-6 col-md-4 col-lg mb-10 mb-md-0">
<h4 class="h6 mb-3">Company</h4>

<ul class="list-unstyled list-sm-space fs-sm mb-0">
<li><a class="link-dark" href="/aboutus">About Us</a></li>
<li><a class="link-dark" href="/brandassets">Brand Assets</a></li>
<li><a class="link-dark" href="/contactus">Contact Us</a></li>
<li>
<a class="link-dark" href="/careers">
<span class="me-1">Careers</span> <span class="bg-primary text-white small fw-medium text-nowrap rounded-pill p-1 px-2">We're Hiring!</span>
</a>
</li>
<li><a class="link-dark" href="/terms">Terms</a> & <a class="link-dark" href="/privacyPolicy">Privacy</a></li>
<li><a class="link-dark" href="/bugbounty">Bug Bounty</a></li>
</ul>

</div>
<div class="col-6 col-md-4 col-lg mb-10 mb-md-0">
<h4 class="h6 mb-3">Community</h4>

<ul class="list-unstyled list-sm-space fs-sm mb-0">
<li><a class="link-dark" href="https://docs.etherscan.io/" target="_blank">API Documentation</a></li>
<li><a class="link-dark" href="https://info.etherscan.com/">Knowledge Base</a></li>
<li><a class="link-dark" href="https://etherscan.freshstatus.io/" rel="nofollow noopener" target="_blank">Network Status</a></li>
<li><a class="link-dark" href="https://info.etherscan.com/newsletters/">Newsletters</a></li>
</ul>

</div>
<div class="col-6 col-md-4 col-lg">
<h4 class="h6 mb-3">Products &amp; Services</h4>

<ul class="list-unstyled list-sm-space fs-sm mb-0">
<li><a class="link-dark" href="/contactusadvertise">Advertise</a></li>
<li><a class="link-dark" href="/eaas">Explorer-as-a-Service (EaaS)</a></li>
<li><a class="link-dark" href="/apis">API Plans</a></li>
<li><a class="link-dark" href="/priority-support">Priority Support</a></li>
<li><a class="link-dark" href="https://blockscan.com" target="_blank">Blockscan <i class="far fa-arrow-up-right-from-square text-muted ms-1"></i></a></li>
<li><a class="link-dark" href="https://chat.blockscan.com/start" target="_blank">Blockscan Chat <i class="far fa-arrow-up-right-from-square text-muted ms-1"></i></a></li>
</ul>

</div>
</div>


<div class="border-top py-4">
<div class="row justify-content-between align-items-center fs-sm">
<div class="col-md mb-2 mb-md-0">
<p class="mb-0">Etherscan © 2024 (A1)</p>
</div>
<div class="col-md text-md-end">
<p class="mb-0">
Donations: <a class="me-1" href="/address/0x71c7656ec7ab88b098defb751b7401b5f6d8976f"><span id="spanDonateAddress" runat="server">0x71c765...d8976f</span></a> <i class="fas fa-heart text-danger"></i>
</p>
</div>
</div>
</div>

</div>
</footer>


<div id="masterDivCookie">
<div class="fixed-bottom text-center" id="divcookie" style="display: none;">
<div class="alert alert-light fade show border shadow-sm d-inline-flex flex-wrap flex-sm-nowrap align-items-sm-center text-start gap-3 mx-3" role="alert">
<p class="text-dark mb-0">
<i class="far fa-cookie-bite text-muted"></i> This website <a href="/terms#cookiestatement" target="_blank">uses cookies to improve your experience</a>. By continuing to use this website, you agree to its <a href="/terms" target="_blank">Terms</a> and <a href="/privacyPolicy" target="_blank">Privacy Policy</a>.
</p>
<button id="btnCookie" type="button" class="btn btn-primary text-nowrap px-4" data-bs-dismiss="alert" aria-label="Close">Got it!</button>
</div>
</div>
</div>

<script src="/assets/vendor/jquery-ui/jquery-ui.min.js?v=24.2.1.2"></script>
<script src="/assets/vendor/jquery-migrate/dist/jquery-migrate.min.js?v=24.2.1.2"></script>
<script src="/assets/vendor/bootstrap/bootstrap.bundle.min.js?v=24.2.1.2"></script>

<script src="/assets/vendor/cubeportfolio/js/jquery.cubeportfolio.min.js?v=24.2.1.2"></script>
<script src="/assets/vendor/clipboard/dist/clipboard.min.js?v=24.2.1.2"></script>

<script src="/assets/js/hs.core.js?v=24.2.1.2"></script>
<script src="/assets/js/components/hs.cubeportfolio.js?v=24.2.1.2"></script>
<script src="/assets/js/custom/combine-js-bottom2.js?v=24.2.1.2"></script>
<script src="/assets/vendor/autocomplete/dist/js/autocomplete.min.js?v=24.2.1.2"></script>
<script src="/assets/js/custom/ether-search.js?v=24.2.1.2"></script>

<script src="/assets/js/app.min.js?v=24.2.1.2"></script>

<script>
        (function () {
            // INITIALIZATION OF CLIPBOARD
            HSCore.components.HSClipboard.init('.js-clipboard');

            let searchAttributes = {
                'name': 'title',
                'img': 'img',
                'rate': 'rate',
                'address': 'address',
                'link': 'link',
                'group': 'group',
                'groupid': 'groupid',
                'website': 'website',
                'is_verified': 'is_checked',
                'ps': 'ps',
                'desc': 'desc',
                'reputation' : 'reputation'
            }

            etherSearchInit({
                id: 'search-panel',
                attributes: searchAttributes
            });
        })();

       
    </script>

<script>
        $(window).on('load', function () {
            myfn_subscribeNewsletter.startFn("#btnSubscribeNewsletter", "#signupSrEmail")
        });

        $(document).on('ready', function () {

            // Get offset timezone of enduser and set to cookie
            const date = new Date();
            const offsetMinutes = date.getTimezoneOffset();
            const offsetHours = Math.abs(offsetMinutes / 60);
            const sign = offsetMinutes > 0 ? '-' : '+';
            offsetHoursFinal = sign + offsetHours;
            writeCookie("etherscan_offset_datetime", offsetHoursFinal, 365);

            // initialization of cubeportfolio
            $.HSCore.components.HSCubeportfolio.init('.cbp');

            const clipboard = new ClipboardJS('.js-clipboard');
            clipboard.on('success', function (e) {
                let toolTip = bootstrap.Tooltip.getInstance(e.trigger);
                var oriTooltip = toolTip._config.originalTitle
               
                toolTip._config.title = 'Copied!';
                toolTip.setContent();
                toolTip.update();

                setTimeout(function () {
                    toolTip._config.title = oriTooltip;
                }, 1000);
            });
        });

    </script>
<script type="text/javascript">
        var sid = 'b898058005e4b0846dc610a9bdedbc83';
        var strGlobal = getCookie("etherscan_switch_age_datetime");
        var strGlobalFee = sessionStorage.getItem("ShowFee");
        var cookieconsent = getCookie("etherscan_cookieconsent");
        var ignoreCopyConfirmation = getCopyAddressConfirmationSetting();
        
        if (cookieconsent !== "True" && document.getElementById("divcookie")) {
            document.getElementById("divcookie").style.display = "block";
        };
          

        function getCookie(cname) {
            var name = cname + "=";
            var ca = document.cookie.split(';');
            for (var i = 0; i < ca.length; i++) {
                var c = ca[i];
                while (c.charAt(0) === ' ') {
                    c = c.substring(1);
                }
                if (c.indexOf(name) === 0) {
                    return c.substring(name.length, c.length);
                }
            }
            return "";
        }

        $("#btnCookie").click(function () {
            $("#divcookie").fadeOut("slow", function () {
                var d = new Date();
                d.setTime(d.getTime() + (1095 * 24 * 60 * 60 * 1000));
                var expires = "expires=" + d.toUTCString();
                document.cookie = "etherscan_cookieconsent=True" + ";" + expires + ";path=/";;
            });
        });

        function handleSearchText(data) {
            searchAddress = false;
            if ($("search-panel").val() == "") {
                $("#hdnSearchText").val("");
                $("#hdnSearchLabel").val("");
            }
        }

        function writeCookie(key, value, days) {
            var date = new Date();
            days = days || 365;
            date.setTime(+ date + (days * 86400000));
            window.document.cookie = key + "=" + value + "; expires=" + date.toGMTString() + "; path=/";
            return value;
        }

        function setThemeMode(mode) {
            writeCookie('displaymode', mode);
        }

        // Note: this function will be called from where need to init the "Copy Address Confirm Modal".
        function openCopyAddressConfirmModal(address, message) {
            $("#addressToCopy").text(address);
            $("#copyAddressConfirmMessage").text(message);

            const clipboard = new ClipboardJS("#btnConfirmCopyAddress");
            document.getElementById('copyAddressConfirmModal').addEventListener('hidden.bs.modal', event => {
                clipboard.destroy();
            });

            const copyAddressConfirmModal = new bootstrap.Modal('#copyAddressConfirmModal', {
                backdrop: true
            })
            copyAddressConfirmModal.show();
        }

        function saveCopyAddressConfirmationSetting(ignoreCopyConfirmation) {
            const copyAddressConfirmationSetting = {
                ignoreCopyConfirmation: ignoreCopyConfirmation,
                expiresOn: Date.now() + 1000 * 60 * 60 * 24 * 30
            };
            localStorage.setItem("copyAddressConfirmationSetting", JSON.stringify(copyAddressConfirmationSetting));
        }

        function getCopyAddressConfirmationSetting() {
            try {
                const settings = localStorage.getItem("copyAddressConfirmationSetting");
                if (settings) {
                    const copyAddressConfirmationSetting = JSON.parse(settings);

                    return copyAddressConfirmationSetting.ignoreCopyConfirmation && copyAddressConfirmationSetting.expiresOn > Date.now();
                }
                else {
                    return false;
                }
            } catch (e) {
                console.log(e);
                return false;
            }
        }

    </script>
<script src="/assets/js/custom/web3.min.js?v=24.2.1.2"></script>
<script type="text/javascript">
        var web3ojb;
        var isTestnet = 'false';
        var chain = 'Mainnet'

        async function addNetwork(type) {
            if (isTestnet != 'true') return;
            if (chain != 'Holesky') return;

            if (type === 'web3') {
                if (typeof ethereum !== 'undefined') {
                    web3ojb = new Web3(ethereum);
                } else if (typeof web3 !== 'undefined') {
                    web3ojb = new Web3(web3.givenProvider);
                } else {
                    web3ojb = new Web3(ethereum);
                }
            }

            if (typeof web3ojb !== 'undefined') {
                var network = 0;
                network = await web3ojb.eth.net.getId();
                netID = network.toString();
                var params;
                if (isTestnet == 'true') {
                    if (chain == "Holesky") {
                        if (netID == "17000") {
                            alert("Holesky Test Network has already been added to Metamask.");
                            return;
                        } else {
                            params = [{
                                chainId: '0x4268',
                                chainName: 'Holesky Test Network',
                                nativeCurrency: {
                                    name: 'ETH',
                                    symbol: 'ETH',
                                    decimals: 18
                                },
                                rpcUrls: ['https://ethereum-holesky.publicnode.com/'],
                                blockExplorerUrls: ['https://holesky.etherscan.io/']
                            }]

                            if (window.ethereum.providers?.length) {
                                let indexProvider = parent.ethereum.providers.findIndex((provider) => provider.isMetaMask);

                                window.ethereum.providers[indexProvider].request({ method: 'wallet_addEthereumChain', params })
                                    .then(() => console.log('Success'))
                                    .catch((error) => console.log("Error", error.message));
                            } else {
                                if (window.ethereum.isMetaMask) {
                                    window.ethereum.request({ method: 'wallet_addEthereumChain', params })
                                        .then(() => console.log('Success'))
                                        .catch((error) => console.log("Error", error.message));
                                } else {
                                    alert("Please Install Metamask")
                                }
                            }

                        }
                    }
                } else {
                    alert('Unable to locate a compatible web3 browser!');
                }
            }
        }
    </script>
</body>
</html>
'''
soup = BeautifulSoup(html_content, 'html.parser')

additional_section = soup.find('section', class_='container-xxl')
additional_content = additional_section.get_text(strip=True)

table_data = []
table_rows = soup.select('tbody tr')
for row in table_rows:
    columns = row.find_all('td')
    if len(columns) == 4:
        address_tag = columns[0].find('a')
        if address_tag:
            address = address_tag['href']
            address_value = re.sub(r'/address/', '', address)

            hash_name = columns[1].get_text(strip=True)
            balance = columns[2].get_text(strip=True)
            txn_count = int(columns[3].get_text(strip=True).replace(',', ''))

            table_data.append({
                'Address': str(address_value),
                'Name_tag': hash_name,
            })
combined_extracted_data = {
    'name': additional_content,  
    'Main': None,  
    'Others':None,  
    'Legacy': None,  
    'subhead': table_data
}
print(combined_extracted_data)
output_file_path = 'Armor.fi.json'
with open(output_file_path, 'w') as json_file:
    json.dump(combined_extracted_data, json_file, indent=4)

print(f'Data has been saved to {output_file_path}')


