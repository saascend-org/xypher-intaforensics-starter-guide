JS = r'''
/* Everything here degrades to a readable page if it fails: the stage explorer renders its first
   stage from markup on load, and every localStorage touch is wrapped. A rep on a locked-down
   browser still gets the guide. */
(function(){
"use strict";

/* ── remembering where they are ──────────────────────────────────────────────
   Reps are entering 20-odd deals across two weeks, so losing the ticks between sessions would
   make the tracker pointless. Per-browser only; nothing leaves the machine. */
var KEY = "ifx-guide-v1";
function load(){
  try { return JSON.parse(localStorage.getItem(KEY) || "{}") || {}; }
  catch(e){ return {}; }
}
function save(st){
  try { localStorage.setItem(KEY, JSON.stringify(st)); } catch(e){ /* private window, fine */ }
}
var state = load();
if (!state.steps) state.steps = {};
if (!Array.isArray(state.deals)) state.deals = [];
if (typeof state.target !== "number") state.target = 0;

/* ── the click-path steps: click to open, tick to complete ───────────────── */
var steps = [].slice.call(document.querySelectorAll(".steps > li"));
/* Open the first row of EACH list, not just the first on the page -- otherwise someone landing on
   "Enter one deal" sees eight collapsed rows with no hint that they open. */
[].slice.call(document.querySelectorAll(".steps")).forEach(function(ul){
  var first = ul.querySelector(":scope > li");
  if (first) first.classList.add("open");
});
steps.forEach(function(li, i){
  var id = li.dataset.step || ("s" + i);
  var head = li.querySelector(".head");
  var tick = li.querySelector(".tick");
  if (state.steps[id]) li.classList.add("done");

  head.addEventListener("click", function(e){
    if (e.target.closest(".tick")) return;      // the tick is its own control
    li.classList.toggle("open");
  });
  head.setAttribute("tabindex","0");
  head.setAttribute("role","button");
  head.addEventListener("keydown", function(e){
    if (e.key === "Enter" || e.key === " "){ e.preventDefault(); li.classList.toggle("open"); }
  });
  if (tick){
    tick.setAttribute("tabindex","0");
    tick.setAttribute("role","button");
    function toggle(){
      li.classList.toggle("done");
      state.steps[id] = li.classList.contains("done");
      save(state);
      paintSteps();
    }
    tick.addEventListener("click", function(e){ e.stopPropagation(); toggle(); });
    tick.addEventListener("keydown", function(e){
      if (e.key === "Enter" || e.key === " "){ e.preventDefault(); e.stopPropagation(); toggle(); }
    });
  }
});
function paintSteps(){
  steps.forEach(function(li){
    var t = li.querySelector(".tick");
    if (t) t.textContent = li.classList.contains("done") ? "Done" : "Mark done";
  });
}
paintSteps();

/* ── stage explorer ─────────────────────────────────────────────────────── */
var STAGES = window.__IFX_STAGES__ || [];
var pick = document.getElementById("stagepick");
var box  = document.getElementById("stagebox");

function esc(s){
  return String(s == null ? "" : s).replace(/[&<>"]/g, function(c){
    return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c];
  });
}
function renderStage(id){
  var s = STAGES.filter(function(x){ return x.id === id; })[0];
  if (!s || !box) return;
  var rows = s.fields.map(function(f){
    var opts = "";
    if (f.opts && f.opts.length){
      /* A rep does not need prose about "grade Engaged or above" -- they need to see which
         options in the dropdown actually let them move on. Green passes, grey does not. */
      opts = '<div class="opts">' + f.opts.map(function(o){
        return '<span class="opt ' + (o[1] ? "y" : "n") + '">' + esc(o[0]) + "</span>";
      }).join("") + "</div>";
    }
    return '<li><span class="f">' + esc(f.f) + "</span>" +
           '<span class="w">' + esc(f.w) + "</span>" + opts +
           (f.note ? '<span class="w">' + esc(f.note) + "</span>" : "") + "</li>";
  }).join("");
  box.innerHTML =
    '<div class="sb-head"><h3>' + esc(s.name) + " &mdash; stage " + s.pos + " of 6</h3>" +
    "<p>" + esc(s.what) + "</p></div>" +
    '<div class="sb-body">' +
      '<div class="legend"><span><span class="opt y">passes the gate</span></span>' +
      '<span><span class="opt n">will not let you move on</span></span></div>' +
      '<ul class="req">' + rows + "</ul>" +
      '<div class="note" style="margin:16px 0 0"><span class="tag">Worth knowing</span><p>' +
      esc(s.rule) + "</p></div>" +
    "</div>";
  [].slice.call(pick.querySelectorAll("button")).forEach(function(b){
    b.setAttribute("aria-pressed", String(b.dataset.stage === id));
  });
}
if (pick){
  pick.addEventListener("click", function(e){
    var b = e.target.closest("button[data-stage]");
    if (b) renderStage(b.dataset.stage);
  });
  if (STAGES.length) renderStage(STAGES[0].id);
}

/* ── pipeline tracker ───────────────────────────────────────────────────── */
var list   = document.getElementById("deals");
var nameIn = document.getElementById("dealname");
var addBtn = document.getElementById("dealadd");
var tgtIn  = document.getElementById("target");
var bar    = document.getElementById("bar");
var cnt    = document.getElementById("count");
var sub    = document.getElementById("progsub");

function paintProgress(){
  var done  = state.deals.filter(function(d){ return d.done; }).length;
  var total = state.deals.length;
  var target = state.target > 0 ? state.target : total;
  if (cnt) cnt.textContent = done + (target ? " / " + target : "");
  var pct = target > 0 ? Math.min(100, Math.round(done / target * 100)) : 0;
  if (bar) bar.style.width = pct + "%";
  if (sub){
    if (!total && !state.target) sub.textContent = "List the deals you want to tidy below and tick them off as you go.";
    else if (done === 0) sub.textContent = total + " listed, none tidied yet.";
    else if (target && done >= target) sub.textContent = "Pipeline tidied. Well done.";
    else sub.textContent = done + " of " + (target || total) + " tidied — " + pct + "% there.";
  }
}
function paintDeals(){
  if (!list) return;
  if (!state.deals.length){
    list.innerHTML = '<p class="empty">Nothing listed yet. Open My Opportunities and add each deal you want to tidy.</p>';
    paintProgress(); return;
  }
  list.innerHTML = state.deals.map(function(d, i){
    return '<div class="deal' + (d.done ? " done" : "") + '">' +
      '<input type="checkbox" data-i="' + i + '"' + (d.done ? " checked" : "") +
      ' aria-label="Entered into Salesforce">' +
      '<input type="text" data-n="' + i + '" value="' + esc(d.name) + '" aria-label="Deal name">' +
      '<button data-x="' + i + '" title="Remove" aria-label="Remove this deal">&times;</button>' +
    "</div>";
  }).join("");
  paintProgress();
}
if (list){
  list.addEventListener("change", function(e){
    var cb = e.target.closest("input[type=checkbox]");
    if (cb){ state.deals[+cb.dataset.i].done = cb.checked; save(state); paintDeals(); }
  });
  list.addEventListener("input", function(e){
    var tx = e.target.closest("input[data-n]");
    if (tx){ state.deals[+tx.dataset.n].name = tx.value; save(state); paintProgress(); }
  });
  list.addEventListener("click", function(e){
    var x = e.target.closest("button[data-x]");
    if (x){ state.deals.splice(+x.dataset.x, 1); save(state); paintDeals(); }
  });
}
function addDeal(){
  var v = (nameIn && nameIn.value || "").trim();
  if (!v) return;
  state.deals.push({ name: v, done: false });
  save(state);
  if (nameIn){ nameIn.value = ""; nameIn.focus(); }
  paintDeals();
}
if (addBtn) addBtn.addEventListener("click", addDeal);
if (nameIn) nameIn.addEventListener("keydown", function(e){ if (e.key === "Enter") addDeal(); });
if (tgtIn){
  tgtIn.value = state.target || "";
  tgtIn.addEventListener("input", function(){
    state.target = parseInt(tgtIn.value, 10) || 0; save(state); paintProgress();
  });
}
var reset = document.getElementById("resetall");
if (reset) reset.addEventListener("click", function(){
  if (!confirm("Clear your ticks and your deal list? This only affects this browser.")) return;
  state = { steps:{}, deals:[], target:0 }; save(state);
  steps.forEach(function(li){ li.classList.remove("done"); });
  paintSteps(); if (tgtIn) tgtIn.value = ""; paintDeals();
});

paintDeals();
})();
'''
