---
tags:
  - weekly
  - task-management
  - 2025-W{{date:ww}}
creation-date: {{date:YYYY-MM-DD}}
---

# 📅 {{date:YYYY年}}第{{date:ww}}週 ({{date:YYYY-MM-DD}} - {{date+6d:YYYY-MM-DD}})

## 📊 今週のDailyノート一覧

```dataviewjs
// 今週の日付範囲を計算
const currentDate = new Date('{{date:YYYY-MM-DD}}');
const weekStart = new Date(currentDate);
weekStart.setDate(currentDate.getDate() - currentDate.getDay()); // 日曜日を週の開始とする

const weekEnd = new Date(weekStart);
weekEnd.setDate(weekStart.getDate() + 6);

// 日付フォーマット関数
function formatDate(date) {
    return date.getFullYear().toString() + 
           (date.getMonth() + 1).toString().padStart(2, '0') + 
           date.getDate().toString().padStart(2, '0');
}

// 今週のDailyノートを取得
const weeklyNotes = [];
for (let d = new Date(weekStart); d <= weekEnd; d.setDate(d.getDate() + 1)) {
    const dateStr = formatDate(d);
    const note = dv.page(`40_Daily/${dateStr}`);
    if (note) {
        weeklyNotes.push({
            date: dateStr,
            note: note,
            dayOfWeek: ['日', '月', '火', '水', '木', '金', '土'][d.getDay()]
        });
    }
}

// テーブルヘッダー
dv.header(3, "📅 今週のDailyノート");
dv.table(["日付", "曜日", "ノート"], 
    weeklyNotes.map(n => [
        n.date,
        n.dayOfWeek,
        n.note.file.link
    ])
);
```

## 📋 今週のタスク一覧

```dataviewjs
// 今週の日付範囲を計算
const currentDate = new Date('{{date:YYYY-MM-DD}}');
const weekStart = new Date(currentDate);
weekStart.setDate(currentDate.getDate() - currentDate.getDay()); // 日曜日を週の開始とする

const weekEnd = new Date(weekStart);
weekEnd.setDate(weekStart.getDate() + 6);

// 日付フォーマット関数
function formatDate(date) {
    return date.getFullYear().toString() + 
           (date.getMonth() + 1).toString().padStart(2, '0') + 
           date.getDate().toString().padStart(2, '0');
}

// 今週のDailyノートを取得
const weeklyNotes = [];
for (let d = new Date(weekStart); d <= weekEnd; d.setDate(d.getDate() + 1)) {
    const dateStr = formatDate(d);
    const note = dv.page(`40_Daily/${dateStr}`);
    if (note) {
        weeklyNotes.push({
            date: dateStr,
            note: note,
            dayOfWeek: ['日', '月', '火', '水', '木', '金', '土'][d.getDay()]
        });
    }
}

// 今週のDailyノートからタスクを抽出
let allTasks = [];

for (let note of weeklyNotes) {
    try {
        const content = await dv.io.load(note.note.file.path);
        const lines = content.split('\n');
        
        let inTodoSection = false;
        const dayTasks = [];
        
        for (let line of lines) {
            if (line.trim() === '## TODO' || line.trim() === '## ✅ タスクリスト') {
                inTodoSection = true;
                continue;
            }
            
            if (inTodoSection && line.trim().startsWith('## ')) {
                inTodoSection = false;
                continue;
            }
            
            if (inTodoSection && line.trim().startsWith('- [')) {
                const isCompleted = line.trim().startsWith('- [x]');
                const taskText = line.trim().substring(4).trim();
                if (taskText) {
                    dayTasks.push({
                        task: taskText,
                        completed: isCompleted,
                        date: note.date
                    });
                }
            }
        }
        
        allTasks.push(...dayTasks);
    } catch (error) {
        console.log(`Error processing ${note.date}:`, error);
    }
}

// タスク一覧を表示
if (allTasks.length > 0) {
    dv.header(3, "📋 今週のタスク一覧");
    dv.table(["日付", "タスク", "完了状況"], 
        allTasks.map(t => [
            t.date,
            t.task,
            t.completed ? "✅ 完了" : "⏳ 未完了"
        ])
    );
} else {
    dv.header(3, "📋 今週のタスク一覧");
    dv.paragraph("今週のタスクはありません。");
}
```

## 📚 今週のSTUDY一覧

```dataviewjs
// 今週の日付範囲を計算
const currentDate = new Date('{{date:YYYY-MM-DD}}');
const weekStart = new Date(currentDate);
weekStart.setDate(currentDate.getDate() - currentDate.getDay()); // 日曜日を週の開始とする

const weekEnd = new Date(weekStart);
weekEnd.setDate(weekStart.getDate() + 6);

// 日付フォーマット関数
function formatDate(date) {
    return date.getFullYear().toString() + 
           (date.getMonth() + 1).toString().padStart(2, '0') + 
           date.getDate().toString().padStart(2, '0');
}

// 今週のDailyノートを取得
const weeklyNotes = [];
for (let d = new Date(weekStart); d <= weekEnd; d.setDate(d.getDate() + 1)) {
    const dateStr = formatDate(d);
    const note = dv.page(`40_Daily/${dateStr}`);
    if (note) {
        weeklyNotes.push({
            date: dateStr,
            note: note,
            dayOfWeek: ['日', '月', '火', '水', '木', '金', '土'][d.getDay()]
        });
    }
}

// 今週のDailyノートからSTUDYを抽出
let allStudy = [];

for (let note of weeklyNotes) {
    try {
        const content = await dv.io.load(note.note.file.path);
        const lines = content.split('\n');
        
        let inStudySection = false;
        const dayStudy = [];
        
        for (let line of lines) {
            if (line.trim() === '## STUDY') {
                inStudySection = true;
                continue;
            }
            
            if (inStudySection && line.trim().startsWith('## ')) {
                inStudySection = false;
                continue;
            }
            
            if (inStudySection && line.trim().startsWith('- ')) {
                const studyText = line.trim().substring(2).trim();
                if (studyText) {
                    dayStudy.push({
                        study: studyText,
                        date: note.date
                    });
                }
            }
        }
        
        allStudy.push(...dayStudy);
    } catch (error) {
        console.log(`Error processing ${note.date}:`, error);
    }
}

// STUDY一覧を表示
if (allStudy.length > 0) {
    dv.header(3, "📚 今週のSTUDY一覧");
    dv.table(["日付", "学習内容"], 
        allStudy.map(s => [
            s.date,
            s.study
        ])
    );
} else {
    dv.header(3, "📚 今週のSTUDY一覧");
    dv.paragraph("今週の学習記録はありません。");
}
```

## 📝 今週のMEMO一覧

```dataviewjs
// 今週の日付範囲を計算
const currentDate = new Date('{{date:YYYY-MM-DD}}');
const weekStart = new Date(currentDate);
weekStart.setDate(currentDate.getDate() - currentDate.getDay()); // 日曜日を週の開始とする

const weekEnd = new Date(weekStart);
weekEnd.setDate(weekStart.getDate() + 6);

// 日付フォーマット関数
function formatDate(date) {
    return date.getFullYear().toString() + 
           (date.getMonth() + 1).toString().padStart(2, '0') + 
           date.getDate().toString().padStart(2, '0');
}

// 今週のDailyノートを取得
const weeklyNotes = [];
for (let d = new Date(weekStart); d <= weekEnd; d.setDate(d.getDate() + 1)) {
    const dateStr = formatDate(d);
    const note = dv.page(`40_Daily/${dateStr}`);
    if (note) {
        weeklyNotes.push({
            date: dateStr,
            note: note,
            dayOfWeek: ['日', '月', '火', '水', '木', '金', '土'][d.getDay()]
        });
    }
}

// 今週のDailyノートからMEMOを抽出
let allMemos = [];

for (let note of weeklyNotes) {
    try {
        const content = await dv.io.load(note.note.file.path);
        const lines = content.split('\n');
        
        let inMemoSection = false;
        const dayMemos = [];
        
        for (let line of lines) {
            if (line.trim() === '## MEMO') {
                inMemoSection = true;
                continue;
            }
            
            if (inMemoSection && line.trim().startsWith('## ')) {
                inMemoSection = false;
                continue;
            }
            
            if (inMemoSection && line.trim().startsWith('- ')) {
                const memoText = line.trim().substring(2).trim();
                if (memoText) {
                    dayMemos.push({
                        memo: memoText,
                        date: note.date
                    });
                }
            }
        }
        
        allMemos.push(...dayMemos);
    } catch (error) {
        console.log(`Error processing ${note.date}:`, error);
    }
}

// MEMO一覧を表示
if (allMemos.length > 0) {
    dv.header(3, "📝 今週のMEMO一覧");
    dv.table(["日付", "メモ"], 
        allMemos.map(m => [
            m.date,
            m.memo
        ])
    );
} else {
    dv.header(3, "📝 今週のMEMO一覧");
    dv.paragraph("今週のメモはありません。");
}
```

## 🎯 今週のEXPERIENCE一覧

```dataviewjs
// 今週の日付範囲を計算
const currentDate = new Date('{{date:YYYY-MM-DD}}');
const weekStart = new Date(currentDate);
weekStart.setDate(currentDate.getDate() - currentDate.getDay()); // 日曜日を週の開始とする

const weekEnd = new Date(weekStart);
weekEnd.setDate(weekStart.getDate() + 6);

// 日付フォーマット関数
function formatDate(date) {
    return date.getFullYear().toString() + 
           (date.getMonth() + 1).toString().padStart(2, '0') + 
           date.getDate().toString().padStart(2, '0');
}

// 今週のDailyノートを取得
const weeklyNotes = [];
for (let d = new Date(weekStart); d <= weekEnd; d.setDate(d.getDate() + 1)) {
    const dateStr = formatDate(d);
    const note = dv.page(`40_Daily/${dateStr}`);
    if (note) {
        weeklyNotes.push({
            date: dateStr,
            note: note,
            dayOfWeek: ['日', '月', '火', '水', '木', '金', '土'][d.getDay()]
        });
    }
}

// 今週のDailyノートからEXPERIENCEを抽出
let allExperiences = [];

for (let note of weeklyNotes) {
    try {
        const content = await dv.io.load(note.note.file.path);
        const lines = content.split('\n');
        
        let inExperienceSection = false;
        const dayExperiences = [];
        
        for (let line of lines) {
            if (line.trim() === '## EXPERIENCE') {
                inExperienceSection = true;
                continue;
            }
            
            if (inExperienceSection && line.trim().startsWith('## ')) {
                inExperienceSection = false;
                continue;
            }
            
            if (inExperienceSection && line.trim().startsWith('- ')) {
                const experienceText = line.trim().substring(2).trim();
                if (experienceText) {
                    dayExperiences.push({
                        experience: experienceText,
                        date: note.date
                    });
                }
            }
        }
        
        allExperiences.push(...dayExperiences);
    } catch (error) {
        console.log(`Error processing ${note.date}:`, error);
    }
}

// EXPERIENCE一覧を表示
if (allExperiences.length > 0) {
    dv.header(3, "🎯 今週のEXPERIENCE一覧");
    dv.table(["日付", "経験・体験"], 
        allExperiences.map(e => [
            e.date,
            e.experience
        ])
    );
} else {
    dv.header(3, "🎯 今週のEXPERIENCE一覧");
    dv.paragraph("今週の経験・体験記録はありません。");
}
```

## 📖 今週のJOURNAL一覧

```dataviewjs
// 今週の日付範囲を計算
const currentDate = new Date('{{date:YYYY-MM-DD}}');
const weekStart = new Date(currentDate);
weekStart.setDate(currentDate.getDate() - currentDate.getDay()); // 日曜日を週の開始とする

const weekEnd = new Date(weekStart);
weekEnd.setDate(weekStart.getDate() + 6);

// 日付フォーマット関数
function formatDate(date) {
    return date.getFullYear().toString() + 
           (date.getMonth() + 1).toString().padStart(2, '0') + 
           date.getDate().toString().padStart(2, '0');
}

// 今週のDailyノートを取得
const weeklyNotes = [];
for (let d = new Date(weekStart); d <= weekEnd; d.setDate(d.getDate() + 1)) {
    const dateStr = formatDate(d);
    const note = dv.page(`40_Daily/${dateStr}`);
    if (note) {
        weeklyNotes.push({
            date: dateStr,
            note: note,
            dayOfWeek: ['日', '月', '火', '水', '木', '金', '土'][d.getDay()]
        });
    }
}

// 今週のDailyノートからJOURNALを抽出
let allJournals = [];

for (let note of weeklyNotes) {
    try {
        const content = await dv.io.load(note.note.file.path);
        const lines = content.split('\n');
        
        let inJournalSection = false;
        const dayJournals = [];
        
        for (let line of lines) {
            if (line.trim() === '## JOURNAL') {
                inJournalSection = true;
                continue;
            }
            
            if (inJournalSection && line.trim().startsWith('## ')) {
                inJournalSection = false;
                continue;
            }
            
            if (inJournalSection && line.trim().startsWith('- ')) {
                const journalText = line.trim().substring(2).trim();
                if (journalText) {
                    dayJournals.push({
                        journal: journalText,
                        date: note.date
                    });
                }
            }
        }
        
        allJournals.push(...dayJournals);
    } catch (error) {
        console.log(`Error processing ${note.date}:`, error);
    }
}

// JOURNAL一覧を表示
if (allJournals.length > 0) {
    dv.header(3, "📖 今週のJOURNAL一覧");
    dv.table(["日付", "日誌"], 
        allJournals.map(j => [
            j.date,
            j.journal
        ])
    );
} else {
    dv.header(3, "📖 今週のJOURNAL一覧");
    dv.paragraph("今週の日誌はありません。");
}
```

---

## 📊 今週の総括

### 🎯 今週の目標達成状況
> 今週設定した目標の達成状況を振り返りましょう。

- **目標1**: 
- **目標2**: 
- **目標3**: 

### 📈 今週の成果
> 今週達成したこと、成果をまとめましょう。

- 
- 
- 

### 🔍 今週の課題・反省
> 今週の課題や改善点を振り返りましょう。

- 
- 
- 

### 💡 来週への改善点
> 来週に向けて改善したい点を整理しましょう。

- 
- 
- 

### 🚀 来週の目標
> 来週の目標を設定しましょう。

- **目標1**: 
- **目標2**: 
- **目標3**: 

### 📅 来週の重要な予定
> 来週の重要な予定や締切を整理しましょう。

- 
- 
- 

---

## 📋 今週の統計

```dataviewjs
// 今週の日付範囲を計算
const currentDate = new Date('{{date:YYYY-MM-DD}}');
const weekStart = new Date(currentDate);
weekStart.setDate(currentDate.getDate() - currentDate.getDay()); // 日曜日を週の開始とする

const weekEnd = new Date(weekStart);
weekEnd.setDate(weekStart.getDate() + 6);

// 日付フォーマット関数
function formatDate(date) {
    return date.getFullYear().toString() + 
           (date.getMonth() + 1).toString().padStart(2, '0') + 
           date.getDate().toString().padStart(2, '0');
}

// 今週のDailyノートを取得
const weeklyNotes = [];
for (let d = new Date(weekStart); d <= weekEnd; d.setDate(d.getDate() + 1)) {
    const dateStr = formatDate(d);
    const note = dv.page(`40_Daily/${dateStr}`);
    if (note) {
        weeklyNotes.push({
            date: dateStr,
            note: note,
            dayOfWeek: ['日', '月', '火', '水', '木', '金', '土'][d.getDay()]
        });
    }
}

// 統計データを収集
let allTasks = [];
let allStudy = [];
let allMemos = [];
let allExperiences = [];
let allJournals = [];

for (let note of weeklyNotes) {
    try {
        const content = await dv.io.load(note.note.file.path);
        const lines = content.split('\n');
        
        let inTodoSection = false;
        let inStudySection = false;
        let inMemoSection = false;
        let inExperienceSection = false;
        let inJournalSection = false;
        
        for (let line of lines) {
            // セクション判定
            if (line.trim() === '## TODO' || line.trim() === '## ✅ タスクリスト') {
                inTodoSection = true;
                inStudySection = false;
                inMemoSection = false;
                inExperienceSection = false;
                inJournalSection = false;
                continue;
            }
            if (line.trim() === '## STUDY') {
                inTodoSection = false;
                inStudySection = true;
                inMemoSection = false;
                inExperienceSection = false;
                inJournalSection = false;
                continue;
            }
            if (line.trim() === '## MEMO') {
                inTodoSection = false;
                inStudySection = false;
                inMemoSection = true;
                inExperienceSection = false;
                inJournalSection = false;
                continue;
            }
            if (line.trim() === '## EXPERIENCE') {
                inTodoSection = false;
                inStudySection = false;
                inMemoSection = false;
                inExperienceSection = true;
                inJournalSection = false;
                continue;
            }
            if (line.trim() === '## JOURNAL') {
                inTodoSection = false;
                inStudySection = false;
                inMemoSection = false;
                inExperienceSection = false;
                inJournalSection = true;
                continue;
            }
            
            // 次のセクションが始まったら全てのセクションを終了
            if (line.trim().startsWith('## ')) {
                inTodoSection = false;
                inStudySection = false;
                inMemoSection = false;
                inExperienceSection = false;
                inJournalSection = false;
                continue;
            }
            
            // タスク処理
            if (inTodoSection && line.trim().startsWith('- [')) {
                const isCompleted = line.trim().startsWith('- [x]');
                const taskText = line.trim().substring(4).trim();
                if (taskText) {
                    allTasks.push({
                        task: taskText,
                        completed: isCompleted,
                        date: note.date
                    });
                }
            }
            
            // STUDY処理
            if (inStudySection && line.trim().startsWith('- ')) {
                const studyText = line.trim().substring(2).trim();
                if (studyText) {
                    allStudy.push({
                        study: studyText,
                        date: note.date
                    });
                }
            }
            
            // MEMO処理
            if (inMemoSection && line.trim().startsWith('- ')) {
                const memoText = line.trim().substring(2).trim();
                if (memoText) {
                    allMemos.push({
                        memo: memoText,
                        date: note.date
                    });
                }
            }
            
            // EXPERIENCE処理
            if (inExperienceSection && line.trim().startsWith('- ')) {
                const experienceText = line.trim().substring(2).trim();
                if (experienceText) {
                    allExperiences.push({
                        experience: experienceText,
                        date: note.date
                    });
                }
            }
            
            // JOURNAL処理
            if (inJournalSection && line.trim().startsWith('- ')) {
                const journalText = line.trim().substring(2).trim();
                if (journalText) {
                    allJournals.push({
                        journal: journalText,
                        date: note.date
                    });
                }
            }
        }
    } catch (error) {
        console.log(`Error processing ${note.date}:`, error);
    }
}

// 統計情報を表示
const completedTasks = allTasks.filter(t => t.completed).length;
const totalTasks = allTasks.length;
const completionRate = totalTasks > 0 ? Math.round((completedTasks / totalTasks) * 100) : 0;

dv.header(3, "📊 今週の統計");
dv.paragraph(`**タスク完了率**: ${completionRate}% (${completedTasks}/${totalTasks})`);
dv.paragraph(`**学習記録数**: ${allStudy.length}件`);
dv.paragraph(`**メモ数**: ${allMemos.length}件`);
dv.paragraph(`**経験・体験記録数**: ${allExperiences.length}件`);
dv.paragraph(`**日誌記録数**: ${allJournals.length}件`);
```

---

## 🔗 関連ノート

```dataviewjs
dv.header(3, "関連ノート");
var maxLoop = Math.min(dv.current().file.tags.length, 3);
for(let i=0;i<maxLoop;i++){
dv.span(dv.current().file.tags[i]);
dv.list(dv.pages(dv.current().file.tags[i]).sort(f=>f.file.mtime.ts,"desc").limit(10).file.link);
}

// バックリンクがあるノートも出力
let backlinks = dv.pages().where(p => p.file.inlinks && p.file.inlinks.map(l=>l.path).includes(dv.current().file.path));
if (backlinks.length > 0) {
    dv.header(4, "このノートへのバックリンク");
    dv.list(backlinks.file.link);
}
```